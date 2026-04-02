# QA Test Case Checklist Tool
# Beginner-friendly project for Day 1–26 of Python

CHECKLIST_FILE = "test_checklist.txt"

def load_checklist():
    checklist = []
    try:
        with open(CHECKLIST_FILE, "r") as file:
            for line in file:
                checklist.append(line.strip())
    except FileNotFoundError:
        pass
    return checklist

def save_checklist(checklist):
    with open(CHECKLIST_FILE, "w") as file:
        for item in checklist:
            file.write(item + "\n")

def show_menu():
    print("\n--- QA Test Case Checklist ---")
    print("1. View checklist")
    print("2. Add test step")
    print("3. Mark step as done")
    print("4. Save and exit")

def view_checklist(checklist):
    if not checklist:
        print("No test steps yet.")
        return
    for i, step in enumerate(checklist, start=1):
        print(f"{i}. {step}")

def add_step(checklist):
    step = input("Enter the test step: ")
    checklist.append("[ ] " + step)
    print("Step added.")

def mark_done(checklist):
    view_checklist(checklist)
    choice = int(input("Which step number is done? "))
    index = choice - 1
    if 0 <= index < len(checklist):
        checklist[index] = checklist[index].replace("[ ]", "[X]")
        print("Step marked as done.")
    else:
        print("Invalid step number.")

def main():
    checklist = load_checklist()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            view_checklist(checklist)
        elif option == "2":
            add_step(checklist)
        elif option == "3":
            mark_done(checklist)
        elif option == "4":
            save_checklist(checklist)
            print("Checklist saved. Goodbye.")
            break
        else:
            print("Invalid option.")

main()
