CONVERSION_THRESHOLD = 100

def convert_to_float(value):
    return float(value)

def sort_mixed_numbers(numbers):
    return sorted(map(convert_to_float, numbers))

if __name__ == '__main__':
    sample_values = ['3.5', 2, '4', 1.1, CONVERSION_THRESHOLD]
    print(sort_mixed_numbers(sample_values))