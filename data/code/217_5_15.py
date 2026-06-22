def compare_numbers(a: int, b: int) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(compare_numbers(num1, num2))
    num1 = 10
    num2 = 10
    print(compare_numbers(num1, num2))
    num1 = 2
    num2 = 8
    print(compare_numbers(num1, num2))