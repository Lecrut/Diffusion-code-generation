import random
def process_selection(choice: str) -> int:
    if choice == "A":
        value = 10 + (random.randint(1, 5)) * 2
    elif choice == "B":
        value = random.choice([3, 7, 9]) ** 2
    else:
        raise ValueError("Invalid selection provided.")
    return value
if __name__ == '__main__':
    sample_choices = ["A", "B"]
    for option in sample_choices:
        result = process_selection(option)
        print(f"Selection {option} yielded the integer: {result}")