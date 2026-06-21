from typing import Sequence

def validate_input(values: Sequence[float]) -> None:
    if not values:
        raise ValueError("The sequence cannot be empty")

def compute_mean(values: Sequence[float]) -> float:
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    validate_input(sample_values)
    mean = compute_mean(sample_values)
    print(f"The mean of the sequence is: {mean}")