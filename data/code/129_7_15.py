def filter_convert_sort(numbers):
    return sorted([int(num) for num in numbers if num > 0])

if __name__ == '__main__':
    sample_numbers = [-2.5, 3.14, -7.89, 0.0, 5.6]
    print(filter_convert_sort(sample_numbers))