from typing import Tuple

def average(numbers: Tuple[int, float]) -> float:
    if not numbers:
        raise ValueError("Input tuple is empty")
    
    total = sum(numbers)
    count = len(numbers)
    
    return total / count

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    print(average(sample_values))