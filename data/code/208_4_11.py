from typing import Sequence

def compute_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence cannot be empty")
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_sequence = [5, 10, 15, 20, 25]
    try:
        result = compute_mean(sample_sequence)
        print(f"The mean of the sequence is: {result}")
    except ValueError as e:
        print(e)