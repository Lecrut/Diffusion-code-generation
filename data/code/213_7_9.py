def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

if __name__ == '__main__':
    test_number = 49
    result = is_perfect_square(test_number)
    print(result)