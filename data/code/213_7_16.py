def is_perfect_square(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    root = int(n ** 0.5)
    return root * root == n

if __name__ == '__main__':
    print(is_perfect_square(16))
    print(is_perfect_square(14))