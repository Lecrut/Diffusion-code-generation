def validate_inputs(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers.')

def compare_numeric(a: int, b: int) -> int:
    validate_inputs(a, b)
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(compare_numeric(num1, num2))
    num1 = 10
    num2 = 10
    print(compare_numeric(num1, num2))
    num1 = 15
    num2 = 8
    print(compare_numeric(num1, num2))