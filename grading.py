import tkinter as tk

master = tk.Tk()

master.title("MARKSHEET")
master.geometry("700x350")

# Entry widgets for subjects
e0 = tk.Entry(master)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)

# Function to display the grades and total
def display():
    grades = []
    subjects = [e4, e5, e6, e7, e8]
    
    # Clear previous results
    for widget in master.grid_slaves():
        if int(widget.grid_info()["row"]) in [3, 4, 5, 6, 7] and int(widget.grid_info()["column"]) == 4:
            widget.destroy()
    
    total_marks = 0
    for i, subject in enumerate(subjects):
        try:
            marks = int(subject.get())
        except ValueError:
            tk.Label(master, text="Invalid").grid(row=3 + i, column=4)
            return
        
        if marks > 100 or marks < 0:
            tk.Label(master, text="Invalid").grid(row=3 + i, column=4)
            return
        
        total_marks += marks
        
        # Assign grades based on marks
        if marks >= 95:
            grade = "A+"
        elif marks >= 90:
            grade = "A"
        elif marks >= 85:
            grade = "B+"
        elif marks >= 80:
            grade = "B"
        elif marks >= 35:
            grade = "PASS"
        else:
            grade = "FAIL"
        
        tk.Label(master, text=grade).grid(row=3 + i, column=4)
        grades.append(grade)
    
    # Display total and SGPA
    tk.Label(master, text=total_marks).grid(row=8, column=3)
    sgpa = total_marks / 50
    tk.Label(master, text=f"{sgpa:.2f}").grid(row=9, column=3)

# Static Labels
tk.Label(master, text="TOTAL").grid(row=8, column=2)
tk.Label(master, text="SGPA").grid(row=9, column=2)

tk.Label(master, text="Name").grid(row=0, column=0)
tk.Label(master, text="SRN No").grid(row=0, column=3)
tk.Label(master, text="Roll.No").grid(row=1, column=0)
tk.Label(master, text="Sec").grid(row=1, column=3)

# Row and column labels
tk.Label(master, text="S.No").grid(row=2, column=0)
tk.Label(master, text="1").grid(row=3, column=0)
tk.Label(master, text="2").grid(row=4, column=0)
tk.Label(master, text="3").grid(row=5, column=0)
tk.Label(master, text="4").grid(row=6, column=0)
tk.Label(master, text="5").grid(row=7, column=0)

# Subject labels
tk.Label(master, text="Subject").grid(row=2, column=1)
tk.Label(master, text="Computer Science").grid(row=3, column=1)
tk.Label(master, text="Civil").grid(row=4, column=1)
tk.Label(master, text="Mathematics").grid(row=5, column=1)
tk.Label(master, text="Electronics").grid(row=6, column=1)
tk.Label(master, text="Chemistry").grid(row=7, column=1)

# Marks entries
tk.Label(master, text="Marks").grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)
e8.grid(row=7, column=2)

# Subject credits labels
tk.Label(master, text="Subject Credits").grid(row=2, column=3)
tk.Label(master, text="5").grid(row=3, column=3)
tk.Label(master, text="4").grid(row=4, column=3)
tk.Label(master, text="5").grid(row=5, column=3)
tk.Label(master, text="4").grid(row=6, column=3)
tk.Label(master, text="5").grid(row=7, column=3)

# Grade labels
tk.Label(master, text="Grade").grid(row=2, column=4)

# User input fields
e0.grid(row=1, column=4)
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

# Submit button
button1 = tk.Button(master, text="Submit", bg="green", command=display)
button1.grid(row=8, column=1)

master.mainloop()