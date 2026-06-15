def generate_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)
if __name__ == '__main__':
    sample_number = 5
    generate_pattern(sample_number)