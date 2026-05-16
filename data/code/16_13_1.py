def filter_positive_numbers(numbers):
    return [x for x in numbers if x > 0]
if __name__ == '__main__':
    sample_list = [1, -2, 3, 0, -4, 5, -7]
    result = filter_positive_numbers(sample_list)
    print(result)