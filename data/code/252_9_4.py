import operator
def compare_numbers(a, b):
    if a < b:
        return "a is less than b"
    elif a > b:
        return "a is greater than b"
    else:
        return "a is equal to b"
if __name__ == '__main__':
    num1 = 15
    num2 = 25
    result = compare_numbers(num1, num2)
    print(result)
    num3 = 100
    num4 = 100
    result2 = compare_numbers(num3, num4)
    print(result2)
    num5 = -5
    num6 = 0
    result3 = compare_numbers(num5, num6)
    print(result3)