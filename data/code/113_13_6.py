def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a - b

if __name__ == '__main__':
    sample_values = {10: 5, 20: 7}
    for num1, num2 in sample_values.items():
        result = subtract_integers(num1, num2)
        print(result)