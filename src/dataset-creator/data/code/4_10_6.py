import sys
def process_choice(choice):
    valid_options = ['a', 'b', 'c']
    if choice in valid_options:
        return f"Processing option {choice}."
    elif choice == 0:
        return "Exiting gracefully. Goodbye!"
    else:
        return f"Invalid input received for '{choice}'. Please try again with a, b, c or 0 to exit."
if __name__ == '__main__':
    sample_inputs = ['a', 'b', 'c', 'd', '', None]
    for item in sample_inputs:
        if isinstance(item, str) and len(str(item).strip()) > 0:
            input_val = str(item).lower().strip()
        elif item is not None:
            try:
                input_val = int(item)
            except ValueError:
                continue
        else:
            continue
        result = process_choice(input_val if isinstance(input_val, (str, int)) else "")
        print(result)