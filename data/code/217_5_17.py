def compare_numbers(a: float, b: float) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    print(compare_numbers(3.5, 2.5))
    print(compare_numbers(-1.0, -1.0))
    print(compare_numbers(0.0, 0.0))
    print(compare_numbers(4.0, 6.0))