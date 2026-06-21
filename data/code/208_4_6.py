from typing import Sequence

mean_calculator = {
    "calculate_mean": lambda values: sum(values) / len(values)
}

def compute_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence cannot be empty")
    return mean_calculator["calculate_mean"](values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        result = compute_mean(sample_values)
        print(f"The mean of the sequence is: {result}")
    except ValueError as e:
        print(e)