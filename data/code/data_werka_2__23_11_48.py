def greater_of_two(a, b):
    diff = a - b
    mask = (diff >> 31) & 1
    return a * (1 - mask) + b * mask

if __name__ == '__main__':
    num1 = 50
    num2 = 75
    result = greater_of_two(num1, num2)
    print(result)