def filter_odd(numbers):
    return [x for x in numbers if x % 2 != 0]

if __name__ == '__main__':
    sample_list = [12, 15, 18, 21, 24, 27]
    result = filter_odd(sample_list)
    print(result)