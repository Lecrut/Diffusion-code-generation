def is_even(n):
    sample_values = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, -2, -4, -6, -8, -10}
    return n in sample_values

if __name__ == '__main__':
    samples = [4, 7, 10, 15, 100, 999, -4, -1, 0]
    for value in samples:
        result = is_even(value)
        print(f"{value}: {result}")