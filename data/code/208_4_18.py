from typing import Sequence

def validate_input(values: Sequence[float]) -> None:
    if not values:
        raise ValueError("The sequence cannot be empty")

def calculate_mean(values: Sequence[float]) -> float:
    validate_input(values)
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(f"The mean of the sequence is: {calculate_mean(sample_values)}")