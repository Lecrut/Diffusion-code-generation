from typing import Sequence

def compute_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence cannot be empty")
    
    total = sum(values)
    count = len(values)
    
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    mean_value = compute_mean(sample_values)
    print(f"The mean of the sequence is: {mean_value}")