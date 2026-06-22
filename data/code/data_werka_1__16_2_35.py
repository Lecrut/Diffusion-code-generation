def is_positive(x):
    return x > 0

if __name__ == '__main__':
    values = [10, -5, 0, 3.14, -0.001]
    for value in values:
        print(is_positive(value))