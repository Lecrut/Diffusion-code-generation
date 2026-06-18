def determine_output(choice):
    if choice == 1:
        return "Option A selected"
    elif choice == 2:
        return "Option B selected"
    elif choice == 3:
        return "Option C selected"
    else:
        return f"Invalid selection. Expected 1, 2, or 3."
if __name__ == '__main__':
    sample_choice = 2
    result = determine_output(sample_choice)
    print(result)