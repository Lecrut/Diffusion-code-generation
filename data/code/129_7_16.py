def filter_convert_sort(numbers):
    return sorted([int(num) for num in numbers if num > 0])

if __name__ == '__main__':
    sample_numbers = [-2.5, 3.14, -1.6, 7.89, 0.0, -3.1]
    print(filter_convert_sort(sample_numbers))