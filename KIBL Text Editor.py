import tkinter as tk
from PIL import Image, ImageTk

# Create the main Tkinter window
root = tk.Tk()
root.title("KBIL Text Editor")

# Load PNG images for each character after creating the root window
images = {
    "K": ImageTk.PhotoImage(Image.open("K.png").resize((40, 65), Image.LANCZOS)),
    "I": ImageTk.PhotoImage(Image.open("I.png").resize((22, 64), Image.LANCZOS)),
    "B": ImageTk.PhotoImage(Image.open("B2.png").resize((35, 75), Image.LANCZOS)),
    "L": ImageTk.PhotoImage(Image.open("L.png").resize((25, 25), Image.LANCZOS)),
}

# Text widget setup with white background
text_widget = tk.Text(root, wrap="word", font=("Arial", 14), bg="white")
text_widget.pack(expand=True, fill="both")

# Bind key event to intercept input and display PNG images for KBIL
def on_key_press(event):
    if event.char in images:  # Check if the character is in our images dictionary
        # Prevent the character from being entered as text
        text_widget.delete("insert -1 chars", "insert")
        
        # Insert the corresponding image in place of the character
        image = images[event.char]
        text_widget.image_create("insert", image=image)
        
        # Store a reference to the image to prevent garbage collection
        if not hasattr(text_widget, "images"):
            text_widget.images = []
        text_widget.images.append(image)
    elif event.char in [" ", "\n", "\t"]:
        # Allow whitespace, new lines, and tabs
        text_widget.insert("insert", event.char)
    elif event.keysym == "BackSpace":
        # Allow backspace to delete the last character or image
        text_widget.delete("insert -1 chars", "insert")
    else:
        # Block any other input
        return "break"

# Bind the key press event to our handler
text_widget.bind("<Key>", on_key_press)

# Run the Tkinter main loop
root.mainloop()
