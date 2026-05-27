# ==========================================
# College Attendance Management System
# Python + MySQL (All-in-One Code)
# ==========================================

import mysql.connector

# --------- DATABASE CONNECTION ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change if required
    password="",        # change if required
    database="college_attendance"
)

cursor = conn.cursor()

# --------- FUNCTIONS ----------

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    year = int(input("Enter Year: "))

    sql = "INSERT INTO students (roll_no, student_name, course, year) VALUES (%s,%s,%s,%s)"
    val = (roll, name, course, year)
    cursor.execute(sql, val)
    conn.commit()
    print("✅ Student added successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Students List ---")
    for row in rows:
        print(row)

def mark_attendance():
    student_id = int(input("Enter Student ID: "))
    subject_id = int(input("Enter Subject ID: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter Status (Present/Absent): ")

    sql = """INSERT INTO attendance 
             (student_id, subject_id, attendance_date, status)
             VALUES (%s,%s,%s,%s)"""
    val = (student_id, subject_id, date, status)
    cursor.execute(sql, val)
    conn.commit()
    print("✅ Attendance marked successfully")

def view_attendance():
    sql = """
    SELECT s.student_name, sub.subject_name, a.attendance_date, a.status
    FROM attendance a
    JOIN students s ON a.student_id = s.student_id
    JOIN subjects sub ON a.subject_id = sub.subject_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n--- Attendance Report ---")
    for row in rows:
        print(row)

def attendance_percentage():
    sql = """
    SELECT s.student_name,
           (SUM(a.status='Present')/COUNT(*))*100 AS percentage
    FROM attendance a
    JOIN students s ON a.student_id = s.student_id
    GROUP BY s.student_name
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\n--- Attendance Percentage ---")
    for row in rows:
        print(row)

# --------- MAIN MENU ----------
while True:
    print("\n====== College Attendance System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Attendance Percentage")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        mark_attendance()
    elif choice == "4":
        view_attendance()
    elif choice == "5":
        attendance_percentage()
    elif choice == "6":
        print("👋 Program Closed")
        break
    else:
        print("❌ Invalid choice")

# --------- CLOSE CONNECTION ----------
cursor.close()
conn.close()
