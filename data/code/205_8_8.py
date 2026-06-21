def sort_mixed_numbers(numbers):
    float_numbers = [float(num) for num in numbers]
    return sorted(float_numbers)

if __name__ == '__main__':
    sample_values = ['3.5', 2, '4', 1.1, '0']
    result = sort_mixed_numbers(sample_values)
    print(result)