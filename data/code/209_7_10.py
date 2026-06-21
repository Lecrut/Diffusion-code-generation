from typing import List, Optional

def validate_data(data: List[float]) -> None:
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements in the list must be numbers.")

def compute_mean(data: List[float]) -> Optional[float]:
    validate_data(data)
    if not data:
        return 0.0
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [7.7, 8.8, 9.9]
    mean_value = compute_mean(sample_data)
    print(mean_value)