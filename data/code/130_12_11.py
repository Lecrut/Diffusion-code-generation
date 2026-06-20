ZERO = 0

def is_zero(value: int) -> bool:
    return value == ZERO

if __name__ == '__main__':
    sample_values = [10, 0, -5, 0, 3.14]
    for value in sample_values:
        result = is_zero(value)
        print(f"Checking value: {value}, Result: {result}")