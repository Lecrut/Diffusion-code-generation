def calculate_max(x, y):
    return (x + y + abs(x - y)) // 2

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    max_value = calculate_max(sample_a, sample_b)
    print(max_value)