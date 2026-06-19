def greater_of_two(a, b):
    difference = a - b
    mask = (difference >> 31) & 1
    return a * (1 - mask) + b * mask

if __name__ == '__main__':
    num1 = 42
    num2 = 27
    result = greater_of_two(num1, num2)
    print(result)