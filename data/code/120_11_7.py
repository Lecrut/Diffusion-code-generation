def strict_equality(a, b):
    return a == b and type(a) is type(b)
if __name__ == '__main__':
    print(strict_equality(5, 5))
    print(strict_equality(5, '5'))
    print(strict_equality([1, 2], [1, 2]))
    print(strict_equality([1, 2], (1, 2)))