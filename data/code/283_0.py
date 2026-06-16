def filter_greater_than_ten(numbers):
    return [x for x in numbers if x > 10]
if __name__ == '__main__':
    sample_list = [5, 12, 8, 15, 3, 22, 9]
    result = filter_greater_than_ten(sample_list)
    print(result)