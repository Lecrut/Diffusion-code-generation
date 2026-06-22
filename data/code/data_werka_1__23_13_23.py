def greater_of_two(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    x = 10
    y = 20
    result = greater_of_two(x, y)
    print(result)