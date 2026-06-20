def filter_sort_convert(numbers):
    return sorted([int(num) for num in numbers if num > 0])

if __name__ == '__main__':
    sample_values = [3.5, -2.1, 4.8, 0.0, -7.6, 2.3]
    result = filter_sort_convert(sample_values)
    print(result)