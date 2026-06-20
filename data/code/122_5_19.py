from typing import Tuple

def calculate_average(numbers: Tuple[int]) -> float:
    if not numbers:
        raise ValueError("The tuple is empty")
    
    total = sum(numbers)
    count = len(numbers)
    
    return total / count

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    average = calculate_average(sample_numbers)
    print(f"The average is: {average}")