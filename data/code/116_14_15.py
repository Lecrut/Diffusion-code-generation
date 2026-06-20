def validate_int(value):
    if not isinstance(value, int):
        raise TypeError("All arguments must be integers")

def sum_three(a: int, b: int, c: int) -> int:
    validate_int(a)
    validate_int(b)
    validate_int(c)
    return a + b + c

if __name__ == '__main__':
    result = sum_three(10, 20, 30)
    print(result)