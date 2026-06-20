def filter_convert_sort(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    integer_numbers = [int(num) for num in positive_numbers]
    sorted_numbers = sorted(integer_numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_numbers = [-2.5, 4.1, -7.89, 0.0, 5.6, 3.3]
    result = filter_convert_sort(sample_numbers)
    print(result)