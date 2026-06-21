def convert_and_sort(numbers):
    float_numbers = list(map(float, numbers))
    sorted_numbers = sorted(float_numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_values = ['7.5', 3, '1.2', 4, 8]
    result = convert_and_sort(sample_values)
    print(result)