task = input("Enter your task for today:")
priority = input("What is the priority level? (high, medium, low):").lower()
time_bound = input("Is this task time_bound? (yes or no):").lower()

match priority:
    case "high":
        reminder = f"High priority: Don't foget to {task}."
    case "medium":
        reminder = f"Medium priority: make time to {task} today."
    case "low":
        reminder = f"Low priority: Try to {task}."
    case _:
        reminder = f" Unknown priority for: {task}"

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

    print("\nYour Daily Reminder:")
    print(reminder)