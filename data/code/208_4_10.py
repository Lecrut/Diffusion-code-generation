from typing import Sequence

MEAN_CALCULATION_THRESHOLD = 1e-9

def calculate_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("The sequence cannot be empty")
    
    total = sum(values)
    count = len(values)
    
    if abs(total / count - (total // count)) < MEAN_CALCULATION_THRESHOLD:
        return total // count
    else:
        return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_values))