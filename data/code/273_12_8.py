def filter_and_double_evens(numbers):
    return [num * 2 for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    result = filter_and_double_evens(sample_list)
    print(result)