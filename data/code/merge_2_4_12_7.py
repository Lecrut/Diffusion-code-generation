import random
def calculate_dynamic_value(choice: int) -> float:
    if choice == 1:
        return sum(range(5)) / len(range(5))
    elif choice == 2:
        product = 1.0
        for i in range(3):
            product *= (i + 1)
        return product
    else:
        raise ValueError("Invalid choice provided.")
def main() -> None:
    choices = [1, 2]
    for selected_choice in random.sample(choices, k=1):
        result = calculate_dynamic_value(selected_choice)
        print(f"Choice {selected_choice} resulted in value: {result}")
if __name__ == '__main__':
    main()