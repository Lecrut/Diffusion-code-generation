import json
def process_choice(choice: str) -> None:
    valid_choices = ["1", "2", "3"]
    if choice in valid_choices:
        actions = {
            "1": print("Action 1 executed successfully."),
            "2": print("Action 2 initiated with high priority."),
            "3": print("Accessing restricted data module.")
        }
        action_func = actions.get(choice)
        if action_func:
            action_func()
    else:
        raise ValueError(f"Invalid choice '{choice}'. Must be one of {valid_choices}.")
if __name__ == '__main__':
    sample_inputs = ["1", "2", "invalid"]
    for input_val in sample_inputs:
        try:
            process_choice(input_val)
        except ValueError as e:
            print(f"Error occurred: {e}")