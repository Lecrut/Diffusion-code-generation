from typing import List, Optional

def find_largest_data_point(data: List[float]) -> Optional[float]:
    if not data:
        return None
    current_max = float('-inf')
    for value in data:
        if value > current_max:
            current_max = value
    return current_max

if __name__ == '__main__':
    sample_input = [23, -10, 45, 100, -99, 67, 33, 88, 12, 55]
    largest = find_largest_data_point(sample_input)
    print(largest)