def greater_of_two(a, b):
    diff = a - b
    mask = (diff >> 31) & 1
    return a * (1 - mask) + b * mask

if __name__ == '__main__':
    x = 42
    y = 27
    print(greater_of_two(x, y))