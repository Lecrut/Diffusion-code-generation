from typing import List

def find_maximum_value(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [12.5, 34.2, 7.8, 90.1, 45.6]
    print(f"Sample Values: {sample_values}")
    try:
        result = find_maximum_value(sample_values)
        print(f"Largest Value: {result}")
    except ValueError as e:
        print(e)