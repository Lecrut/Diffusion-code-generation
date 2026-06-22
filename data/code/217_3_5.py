def max_without_conditional(a, b):
    return (a * (a >= b) + b * (b > a))

if __name__ == '__main__':
    a = 5
    b = 3
    print(max_without_conditional(a, b))