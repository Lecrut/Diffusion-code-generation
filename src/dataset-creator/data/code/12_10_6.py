def is_odd(n):
    return n & 1 != 0
def check_number(num):
    if num < -2 ** 63:
        raise OverflowError("Integer too small")
    elif num > 2 ** 63 - 1:
        raise OverflowError("Integer too large")
    status = "odd" if is_odd(num) else "even"
    return f"{num} is {status}"
if __name__ == '__main__':
    test_cases = [-5, -4, 0, 1, 2, 3]
    for case in test_cases:
        result = check_number(case)
        print(result)