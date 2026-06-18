import random
def process_selection(choice: int) -> str:
    if choice == 1:
        result = "Option A selected."
    elif choice == 2:
        result = f"Option B selected. Random value generated: {random.randint(0, 9)}."
    else:
        result = "Invalid option provided."
    return result
if __name__ == '__main__':
    sample_choices = [1, 2]
    for choice in sample_choices:
        output_message = process_selection(choice)
        print(output_message)