from typing import List, Optional

def compute_mean(data: List[float]) -> Optional[float]:
    if not data:
        raise ValueError("Data list cannot be empty")
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [7.7, 8.8, 9.9]
    try:
        mean_value = compute_mean(sample_data)
        print(mean_value)
    except ValueError as e:
        print(e)