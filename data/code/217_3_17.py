def max_without_conditional(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    x = 15
    y = 9
    print(max_without_conditional(x, y))