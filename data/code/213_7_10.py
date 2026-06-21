def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

if __name__ == '__main__':
    sample_number = 36
    result = is_perfect_square(sample_number)
    print(result)