def strict_equality_check(a, b):
    return a == b
if __name__ == '__main__':
    print(strict_equality_check(5, 5))
    print(strict_equality_check(5, '5'))
    print(strict_equality_check([1, 2], [1, 2]))
    print(strict_equality_check([1, 2], (1, 2)))