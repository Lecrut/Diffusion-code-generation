ODD_BIT_MASK = 1
TEST_CASES = [0, 1, 2, 9, 10, -1, -4, 2147483647]

def is_even(n):
    return (n & ODD_BIT_MASK) == 0

if __name__ == '__main__':
    for value in TEST_CASES:
        print(is_even(value))