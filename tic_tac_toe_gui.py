import tkinter as tk
import random
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe - User vs AI")


board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def ai_move():
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if not empty: return
    row, col = random.choice(empty)
    board[row][col] = "O"
    buttons[row][col].config(text="O", state="disabled")

    if check_winner("O"):
        messagebox.showinfo("Game Over", "AI wins! 😈")
        window.destroy()
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        window.destroy()

def on_click(row, col):
    if board[row][col] == "":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You win! 🎉")
            window.destroy()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            window.destroy()
        else:
            ai_move()


for i in range(3):
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 30), width=5, height=2,
                           command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        buttons[i][j] = button

window.mainloop()
