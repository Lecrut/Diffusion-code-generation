import math

def is_negative(n: int) -> bool:
    return n < 0

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 42]
    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")