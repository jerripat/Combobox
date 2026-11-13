
import customtkinter as ctk

# Set appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create main window
root = ctk.CTk()
root.title("CustomTkinter Combobox Example")
root.geometry("700x450")

# Function to change the label color
def color_picker(choice=None):
    if choice is None:
        choice = my_combobox.get()

    output_label.configure(
        text=f"You picked {choice}",
        text_color=choice
    )


# Instruction label
my_label = ctk.CTkLabel(
    root,
    text="Pick a color from the combobox below",
    font=("Arial", 20)
)
my_label.pack(pady=40)

# Combobox
my_combobox = ctk.CTkComboBox(
    root,
    values=["Red", "Green", "Blue", "Yellow", "Purple"],
    command=color_picker,
    state="readonly",
    width=200,
    font=("Arial", 16)
)
my_combobox.pack(pady=20)

# Set default selection
my_combobox.set("Red")

# Button
my_button = ctk.CTkButton(
    root,
    text="Pick Color",
    command=color_picker,
    width=150,
    height=40
)
my_button.pack(pady=20)

# Output label
output_label = ctk.CTkLabel(
    root,
    text="",
    font=("Arial", 24, "bold")
)
output_label.pack(pady=20)

# Start application
root.mainloop()
