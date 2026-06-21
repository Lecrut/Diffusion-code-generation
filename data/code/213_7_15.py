import math

PERFECT_SQUARE_THRESHOLD = 0

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

if __name__ == '__main__':
    sample_number = 25
    result = is_perfect_square(sample_number)
    print(result)