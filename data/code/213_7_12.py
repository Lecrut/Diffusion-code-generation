import math

MAX_ROOT = int(math.sqrt(2**31 - 1))

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n and root <= MAX_ROOT

if __name__ == '__main__':
    sample_number = 49
    result = is_perfect_square(sample_number)
    print(result)