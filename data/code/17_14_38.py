def is_even(n):
    return (n & 1) == 0

EVEN_CHECK_THRESHOLD = 5

if __name__ == '__main__':
    sample_values = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, EVEN_CHECK_THRESHOLD]
    for value in sample_values:
        print(f"{value} is even: {is_even(value)}")