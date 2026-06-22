from typing import Tuple

def average(numbers: Tuple[float]) -> float:
    if not numbers:
        raise ValueError("Input tuple is empty")
    
    total = sum(numbers)
    count = len(numbers)
    
    return total / count

if __name__ == '__main__':
    sample_values = (10.5, 20.3, 30.7)
    print(average(sample_values))