def max_without_conditional(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    a = 5
    b = 3
    print(max_without_conditional(a, b))