def filter_sort_convert(numbers):
    return sorted([int(num) for num in numbers if num > 0])

if __name__ == '__main__':
    sample_values = [-2.5, 3.14, -7, 8.9, 0, 5]
    print(filter_sort_convert(sample_values))