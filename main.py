import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from spot_diff import spot_diff
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall

window = tk.Tk()
window.title("ASS")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('590x620')
window.configure(bg='black')


frame1 = tk.Frame(window, bg='black')
'''
label_title = tk.Label(frame1, text="Automated Security System", width=35, fg='white', bg='grey')
label_font = font.Font(size=10, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(row=2, pady=(10,10))

'''
icon = Image.open('icons/opic.png')
icon = icon.resize((120,120), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg='black')
label_icon.grid(row=1, pady=(10,10), column=1)

btn1_image = Image.open('icons/sec.png')
btn1_image = btn1_image.resize((50,50), Image.Resampling.LANCZOS )
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/robbery.png')
btn2_image = btn2_image.resize((50,50), Image.Resampling.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.Resampling.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/alarm.png')
btn3_image = btn3_image.resize((50,50), Image.Resampling.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/one-way.png')
btn6_image = btn6_image.resize((50,50), Image.Resampling.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/rec.png')
btn4_image = btn4_image.resize((50,50), Image.Resampling.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/frg.png')
btn7_image = btn7_image.resize((50,50), Image.Resampling.LANCZOS)
btn7_image = ImageTk.PhotoImage(btn7_image)
'''
btn8_image = Image.open('icons/spot.png')
btn8_image = btn8_image.resize((50,50), Image.Resampling.LANCZOS)
btn8_image = ImageTk.PhotoImage(btn8_image)
'''


# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, height=100, width=100, fg='green',bg='black',command = find_motion, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, height=100, width=100, fg='orange',bg='black', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=1, padx=(20,10))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, height=100, width=100, fg='green', bg='black', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=4, column=2, pady=(20,10))

btn4 = tk.Button(frame1, height=100, width=100, fg='orange', bg='black', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=3, pady=(20,10), column=2)


btn6 = tk.Button(frame1, height=100, width=100, fg='green', bg='black' , command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10), column=1)

btn5 = tk.Button(frame1, height=100, width=100, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=4, column=1, pady=(20,10))

btn7 = tk.Button(frame1, fg="orange",bg='black', command=maincall, compound='left', image=btn7_image, height=100, width=100)
btn7['font'] = btn_font
btn7.grid(row=4, pady=(20,10))
'''
btn8 = tk.Button(frame1, fg="orange",bg='black', command=spot_diff, compound='left', image=btn8_image, height=100, width=100)
btn8['font'] = btn_font
btn8.grid(row=5, pady=(20,10))
'''
frame1.pack()
window.mainloop()


