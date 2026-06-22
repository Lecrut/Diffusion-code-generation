from typing import Tuple

def average(numbers: Tuple[int, float]) -> float:
    if not numbers:
        raise ValueError("Input tuple is empty")
    
    total = 0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Tuple contains non-numeric types")
        total += num
    
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40)
    print(average(sample_values))