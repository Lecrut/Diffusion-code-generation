from typing import List, Optional

def compute_mean(data: List[float]) -> Optional[float]:
    if not data:
        return None
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [7.7, 8.8, 9.9]
    result = compute_mean(sample_data)
    print(result)