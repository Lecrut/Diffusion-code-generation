def filter_positives(numbers):
    return [x for x in numbers if x > 0]
if __name__ == '__main__':
    sample_list = [1, -2, 3, 0, -5, 6, 7, -8]
    result = filter_positives(sample_list)
    print(result)