# ============================================
# Railway Management System (Final Version)
# Admin: Station + Train Management
# User: Reservation
# Author: Sanchit Singh
# ============================================

import mysql.connector

# ================= DB CONNECTION =================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="railway"
)
cursor = db.cursor()

# =================================================
# ADMIN LOGIN
# =================================================
def admin_login():
    print("\n--- Admin Login Required ---")
    user = input("Username: ")
    pwd = input("Password: ")

    if user == "admin" and pwd == "1234":
        print("✅ Login Successful")
        return True
    else:
        print("❌ Access Denied")
        return False

# =================================================
# STATION MANAGEMENT (ADMIN)
# =================================================
def add_station():
    name = input("Station Name: ")
    code = input("Station Code: ")
    city = input("City: ")
    platforms = int(input("Platforms: "))

    sql = """INSERT INTO station
    (station_name, station_code, city, platforms)
    VALUES (%s,%s,%s,%s)"""

    cursor.execute(sql, (name, code, city, platforms))
    db.commit()
    print("✅ Station Added")

def view_stations():
    cursor.execute("SELECT * FROM station")
    for row in cursor.fetchall():
        print(row)

def delete_station():
    sid = input("Station ID to delete: ")
    cursor.execute("DELETE FROM station WHERE station_id=%s", (sid,))
    db.commit()
    print("🗑 Station Deleted")

# =================================================
# TRAIN MANAGEMENT (ADMIN)
# =================================================
def add_train():
    name = input("Train Name: ")
    seats = int(input("Total Seats: "))

    cursor.execute(
        "INSERT INTO train (train_name,total_seats) VALUES (%s,%s)",
        (name, seats)
    )
    db.commit()
    print("🚆 Train Added")

def view_trains():
    cursor.execute("SELECT * FROM train")
    for row in cursor.fetchall():
        print(row)

def delete_train():
    tid = input("Train ID to delete: ")
    cursor.execute("DELETE FROM train WHERE train_id=%s", (tid,))
    db.commit()
    print("🚆 Train Deleted")

# =================================================
# ADMIN MENU
# =================================================
def admin_menu():
    if not admin_login():
        return

    while True:
        print("\n===== ADMIN PANEL =====")
        print("1. Add Station")
        print("2. View Stations")
        print("3. Delete Station")
        print("4. Add Train")
        print("5. View Trains")
        print("6. Delete Train")
        print("7. Back")

        ch = input("Choice: ")

        if ch == "1":
            add_station()
        elif ch == "2":
            view_stations()
        elif ch == "3":
            delete_station()
        elif ch == "4":
            add_train()
        elif ch == "5":
            view_trains()
        elif ch == "6":
            delete_train()
        elif ch == "7":
            break

# =================================================
# PASSENGER (USER)
# =================================================
def add_passenger():
    name = input("Passenger Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")

    cursor.execute(
        "INSERT INTO passenger (name,age,gender) VALUES (%s,%s,%s)",
        (name, age, gender)
    )
    db.commit()
    print("👤 Passenger Added")

# =================================================
# RESERVATION (USER)
# =================================================
def book_ticket():
    print("\n--- Available Trains ---")
    view_trains()

    passenger_id = int(input("Passenger ID: "))
    train_id = int(input("Train ID: "))

    print("\n--- Available Stations ---")
    view_stations()

    source = int(input("Source Station ID: "))
    dest = int(input("Destination Station ID: "))
    date = input("Journey Date (YYYY-MM-DD): ")
    seat = input("Seat Number: ")

    sql = """INSERT INTO reservation
    (passenger_id,train_id,source_station,destination_station,journey_date,seat_number)
    VALUES (%s,%s,%s,%s,%s,%s)"""

    cursor.execute(sql, (passenger_id, train_id, source, dest, date, seat))
    db.commit()
    print("🎫 Ticket Booked")

def view_reservations():
    cursor.execute("SELECT * FROM reservation")
    for row in cursor.fetchall():
        print(row)

# =================================================
# USER MENU
# =================================================
def user_menu():
    while True:
        print("\n===== USER PANEL =====")
        print("1. Add Passenger")
        print("2. Book Ticket")
        print("3. View Reservations")
        print("4. Back")

        ch = input("Choice: ")

        if ch == "1":
            add_passenger()
        elif ch == "2":
            book_ticket()
        elif ch == "3":
            view_reservations()
        elif ch == "4":
            break

# =================================================
# MAIN MENU
# =================================================
while True:
    print("\n===== Railway Management System =====")
    print("1. Admin Panel")
    print("2. User Panel")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        admin_menu()
    elif choice == "2":
        user_menu()
    elif choice == "3":
        print("🚆 Thank You")
        break
