from typing import Sequence

def calculate_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence is empty")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_mean(sample_values)
        print(f"The mean of the values is: {mean_value}")
    except ValueError as e:
        print(e)