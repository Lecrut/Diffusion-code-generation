from typing import Tuple

def calculate_average(numbers: Tuple[int, float]) -> float:
    if not numbers:
        raise ValueError("Input tuple is empty")
    
    total_sum = 0.0
    count = 0
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Tuple contains non-numeric types")
        
        total_sum += num
        count += 1
    
    return total_sum / count

if __name__ == '__main__':
    sample_values = (5, 10, 15, 20, 25)
    try:
        avg = calculate_average(sample_values)
        print(f"The average is: {avg}")
    except ValueError as e:
        print(e)