import random
def select_dynamic_option(choice: int) -> str:
    options = {
        1: "Option A selected",
        2: "Option B selected",
        3: "Option C selected"
    }
    if choice in options:
        return options[choice]
    raise ValueError(f"Invalid option chosen. Must be between 1 and {len(options)}")
if __name__ == '__main__':
    sample_choice = random.randint(1, len({"a": "A", "b": "B"}))
    result = select_dynamic_option(sample_choice)
    print(result)