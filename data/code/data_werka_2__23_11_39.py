def greater_of_two(a, b):
    difference = a - b
    sign = difference >> 31 & 1
    return a * (1 - sign) + b * sign
if __name__ == '__main__':
    num1 = 50
    num2 = 75
    result = greater_of_two(num1, num2)
    print(result)