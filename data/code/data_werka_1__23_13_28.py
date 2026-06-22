def greater_of_two(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    x = 10
    y = 20
    print(greater_of_two(x, y))