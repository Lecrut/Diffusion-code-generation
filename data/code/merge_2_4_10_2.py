def determine_output(choice):
    if choice == 1:
        return "Option A selected"
    elif choice == 2:
        return "Option B selected"
    elif choice == 3:
        return "Option C selected"
    else:
        return "Invalid option chosen"
if __name__ == '__main__':
    sample_choices = [1, 2, -5, 0]
    for c in sample_choices:
        try:
            result = determine_output(c)
            print(f"Input {c}: Output is '{result}'")
        except Exception as e:
            print(f"Error processing input {c}: {e}")