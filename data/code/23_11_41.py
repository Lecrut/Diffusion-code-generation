def greater_of_two(a, b):
    diff = a - b
    sign = (diff >> 31) & 1
    return a - sign * diff

if __name__ == '__main__':
    result = greater_of_two(10, 20)
    print(result)