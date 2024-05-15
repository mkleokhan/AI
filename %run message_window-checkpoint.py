{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da6b8f4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "import winsound\n",
    "\n",
    "def play_default_sound():\n",
    "    winsound.PlaySound(\"SystemAsterisk\", winsound.SND_ALIAS)\n",
    "\n",
    "# Function to center the window on the screen\n",
    "def center_window(window, width, height):\n",
    "    screen_width = window.winfo_screenwidth()\n",
    "    screen_height = window.winfo_screenheight()\n",
    "    x_coordinate = (screen_width - width) // 2\n",
    "    y_coordinate = (screen_height - height) // 2\n",
    "    window.geometry(f\"{width}x{height}+{x_coordinate}+{y_coordinate}\")\n",
    "\n",
    "# Create a window\n",
    "window = tk.Tk()\n",
    "\n",
    "# Set the window title\n",
    "window.title(\"Message Display\")\n",
    "\n",
    "# Create a bold font\n",
    "bold_font = (\"Arial\", 12, \"bold\")\n",
    "\n",
    "# Create a label with the message\n",
    "message = \"Completed\"\n",
    "label = tk.Label(window, text=message, font=bold_font)\n",
    "label.pack()\n",
    "\n",
    "# Play default system sound\n",
    "play_default_sound()\n",
    "\n",
    "# Set window size\n",
    "window_width = 200\n",
    "window_height = 200\n",
    "\n",
    "# Center the window on the screen\n",
    "center_window(window, window_width, window_height)\n",
    "\n",
    "# Run the window\n",
    "window.mainloop()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
