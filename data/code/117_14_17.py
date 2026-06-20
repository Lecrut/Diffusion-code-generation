import math

def validate_numbers(a: int, b: int) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def calculate_signed_difference(a: int, b: int) -> int:
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = calculate_signed_difference(sample_a, sample_b)
    print(f"The signed difference between {sample_a} and {sample_b} is {result}")