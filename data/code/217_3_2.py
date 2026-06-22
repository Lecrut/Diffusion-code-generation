def max_without_conditional(a, b):
    return (a + b) / 2 + abs((a - b)) / 4

if __name__ == '__main__':
    x = 10
    y = 7
    print(max_without_conditional(x, y))