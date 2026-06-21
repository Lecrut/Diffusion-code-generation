from typing import Sequence

def calculate_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence cannot be empty")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        result = calculate_mean(sample_values)
        print(f"The mean of the sequence is: {result}")
    except ValueError as e:
        print(e)