def compare_numbers(a: int, b: int) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result = compare_numbers(5, 3)
    print(result)