from tkinter import *
import math

window = Tk()


def cal():
    while True:
        try:
            global ep_entry
            global stop_entry
            global tp_entry

            ep = ep_entry.get()
            sl = stop_entry.get()
            tp = tp_entry.get()

            ep_float = float(ep)
            sl_float = float(sl)
            tp_float = float(tp)

            if ep_float > sl_float:
                origin_ep = ep_float
                origin_sl = sl_float

                cal_sl = (origin_ep - origin_sl) / 0.0001
                print(round(cal_sl))

            elif sl_float > ep_float:
                origin_ep = sl_float
                origin_sl = ep_float

                cal_sl = (origin_ep - origin_sl) / 0.0001
                print(round(cal_sl))

            # tp
            if ep_float > tp_float:
                origin_ep = ep_float
                origin_tp = tp_float

                cal_tp = (origin_ep - origin_tp) / 0.0001


            elif tp_float > ep_float:
                origin_ep = tp_float
                origin_tp = ep_float

                cal_tp = (origin_ep - origin_tp) / 0.0001

            # Risk to reward ratio Calculation
            r2r_ratio = cal_tp / cal_sl
            rounding_ = round(r2r_ratio)
            remainder = cal_tp % cal_sl + 1
            rounding_rem = round(remainder)

            # Confirming Whether it is a good Entry Or Not
            if rounding_ > rounding_rem:
                good_text = ("Good Entry!\n"
                             "Give it a go!")

            else:
                good_text = ("Bad Choice Mate!\n"
                             "Poor Choice!")

            # Display Results
            answer_label = Label(window,
                                 text="Stop Loss: {} pips\n"
                                      "Take Profit: {} pips\n"
                                      "Risk to Reward Ratio: {}:{}\n"
                                      "\n"
                                      "{}".format(math.ceil(cal_sl),
                                                  math.ceil(cal_tp),
                                                  math.ceil(rounding_),
                                                  math.ceil(rounding_rem), good_text),

                                 font=("comic sans", 10, "bold"),
                                 width=50,
                                 height=6,
                                 foreground="black",
                                 justify="center",
                                 background="white")
            answer_label.place(x=0, y=515)
            break

        except ValueError:
            print("Hey, Dummy!\n"
                  "Enter something meaningful!!!!")
            print()
            break

    # Clear Entry Box
    ep_entry.delete(0, END)
    stop_entry.delete(0, END)
    tp_entry.delete(0, END)


window.title("Pip Calculator")
window.geometry("400x620")
window.resizable(0, 0)
window.config(background="indigo")

ep_label = Label(text="ENTRY PRICE(EP):",
                 background="indigo",
                 font=("arial", 20, "bold"),
                 foreground="white")

ep_label.place(x=30, y=50)
ep_entry = Entry(width=30,
                 textvariable="float",
                 font=("comic sans", 15, "bold"),
                 justify="center",
                 )
ep_entry.place(x=30, y=90)

# stop-loss
stop_label = Label(text="STOP LOSS(SL):",
                   background="indigo",
                   font=("comic sans", 20, "bold"),
                   foreground="white")

stop_label.place(x=30, y=150)
stop_entry = Entry(width=30,
                   font=("comic sans", 15, "bold"),
                   justify="center")
stop_entry.place(x=30, y=190)

# take-profit
tp_label = Label(text="TAKE-PROFIT(TP):",
                 background="indigo",
                 font=("comic sans", 20, "bold"),
                 foreground="white")

tp_label.place(x=30, y=250)
tp_entry = Entry(width=30,
                 textvariable=StringVar(),
                 font=("comic sans", 15, "bold"),
                 justify="center")
tp_entry.place(x=30, y=290)

# Lot-size

cal_button = Button(text="Analyse Data",
                    width=20,
                    height=2,
                    background="black",
                    font=("comic sans", 10, "bold"),
                    foreground="white",
                    command=cal,
                    )

cal_button.place(x=100, y=380)

window.mainloop()
