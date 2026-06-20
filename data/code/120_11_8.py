def strict_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(strict_equality(1, 1))
    print(strict_equality(1, '1'))
    print(strict_equality([1, 2], [1, 2]))
    print(strict_equality([1, 2], (1, 2)))