CONVERSION_FACTOR = 1.0

def sort_mixed_numbers(numbers):
    return sorted(map(lambda x: float(x * CONVERSION_FACTOR), numbers))

if __name__ == '__main__':
    sample_values = ['3.5', 2, '4', 1.1]
    print(sort_mixed_numbers(sample_values))