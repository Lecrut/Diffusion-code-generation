import sys
def strategy_one():
    return "Execution path 1 selected."
def strategy_two():
    return "Execution path 2 selected."
def strategy_three():
    return "Execution path 3 selected."
if __name__ == '__main__':
    try:
        choice = int(sys.argv[1]) if len(sys.argv) > 1 else None
        valid_choices = [1, 2, 3]
        if not (choice in valid_choices):
            print(f"Invalid choice. Please select from {valid_choices}.")
            sys.exit(0)
        result_map = {
            1: strategy_one,
            2: strategy_two,
            3: strategy_three
        }
        selected_func = result_map.get(choice)
        if not selected_func:
            print("No valid function mapped to this choice.")
            sys.exit(0)
        output = selected_func()
        print(output)
    except ValueError:
        print("Error: Input must be an integer.")
        sys.exit(1)