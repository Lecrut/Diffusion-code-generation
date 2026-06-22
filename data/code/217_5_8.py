def compare_values(a: int, b: int) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    num1 = 7
    num2 = 3
    print(compare_values(num1, num2))
    num1 = 4
    num2 = 8
    print(compare_values(num1, num2))
    num1 = 6
    num2 = 6
    print(compare_values(num1, num2))