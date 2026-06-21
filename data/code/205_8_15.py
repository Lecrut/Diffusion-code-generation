def sort_mixed_numbers(numbers):
    float_numbers = list(map(float, numbers))
    sorted_numbers = sorted(float_numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_values = ['2.5', 3, '1.1', 4.8]
    result = sort_mixed_numbers(sample_values)
    print(result)