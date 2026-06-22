def compare_numbers(a: int, b: int) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    print(compare_numbers(3, 5))
    print(compare_numbers(7, 2))
    print(compare_numbers(4, 4))