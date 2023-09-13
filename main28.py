from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC_IN_A_MIN = 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer() -> None:
    """Reset the timer, and place the 00:00 on screen"""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer() -> None:
    """Start the timer count considering which countdown need to be shown: work time, short break or long break"""
    global reps
    work_sec = WORK_MIN * SEC_IN_A_MIN
    short_break_sec = SHORT_BREAK_MIN * SEC_IN_A_MIN
    long_break_sec = LONG_BREAK_MIN * SEC_IN_A_MIN
    reps += 1
    if reps == 8:
        count_down(long_break_sec)
        title.config(text="Break", fg=GREEN)
        window.attributes('-topmost', 1)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=GREEN)
        window.attributes('-topmost', 1)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=RED)
        window.attributes('-topmost', 1)

    #  reset repetitions after long break (8th rep)
    if reps > 8:
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count: int) -> None:
    """Execute the appropriate countdown and display correct time visualization"""
    global reps, timer
    window.attributes('-topmost', 0)
    count_min = math.floor(count / SEC_IN_A_MIN)
    count_sec = count % SEC_IN_A_MIN
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        # work_sessions = math.floor(reps/2)
        # for _ in range(work_sessions):
        #     marks = "✔"
        # check.config(text=marks)
        if reps % 2 == 0:
            half = int(reps/2)
            marks = half*"✔"
            check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", font=(FONT_NAME, 13), bg=GREEN, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 13), bg=PINK, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)
window.mainloop()
