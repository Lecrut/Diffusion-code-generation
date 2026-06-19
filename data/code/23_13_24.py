def find_greater(a, b):
    difference = a - b
    mask = (difference >> 31) & 1
    return a * (1 - mask) + b * mask

if __name__ == '__main__':
    num1 = 42
    num2 = 27
    greater_number = find_greater(num1, num2)
    print(greater_number)