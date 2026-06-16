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
    sample_choices = [1, 2, 3, -5]
    for choice in sample_choices:
        result = determine_output(choice)
        print(f"Input: {choice} -> Output: {result}")