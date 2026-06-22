from typing import List
import statistics

def compute_min_max(data: List[float]) -> Tuple[float, float]:
    return min(data), max(data)

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 4.8, 2.9, 5.1]
    min_val, max_val = compute_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")