from typing import List, Optional

def calculate_average(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [7.7, 8.8, 9.9]
    result = calculate_average(sample_values)
    print(result)