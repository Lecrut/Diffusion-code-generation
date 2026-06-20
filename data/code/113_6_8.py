def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    sample_values = [(100, 45), (50, 150)]
    for a, b in sample_values:
        result = subtract_numbers(a, b)
        print(f"Result of {a} - {b}: {result}")