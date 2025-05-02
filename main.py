from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)  # Cancel the current timer
        timer = None  # Reset the timer variable
    canvas.itemconfig(timer_text, text="00:00")
    my_lable.config(text="Timer")
    check_marks.config(text="")
    reps = 0
        # Re-enable the Start button
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer
    reps += 1
    # Disable the Start button after the first press
    start_button.config(state="disabled")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        my_lable.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        my_lable.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        my_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "🎯"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- 
window = Tk()
window.title("Focus")
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image =tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

my_lable = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45),highlightthickness=0)
my_lable.grid(row=1,column=2)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)

start_button.grid(row=3,column=1)
reset_button.grid(row=3,column=3)

large_font = ("Arial", 30)
check_marks = Label(fg=GREEN,bg=YELLOW,font=large_font)
check_marks.grid(row=4,column=2)




canvas.mainloop()

