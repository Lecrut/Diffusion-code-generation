def filter_convert_sort(numbers):
    return sorted([int(num) for num in numbers if num > 0])

if __name__ == '__main__':
    sample_numbers = [3.5, -2.1, 4.8, 0, -1.7, 6.0]
    result = filter_convert_sort(sample_numbers)
    print(result)