def filter_odd_numbers(data):
    return [x for x in data if x % 2 != 0]
if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd_numbers(input_list)
    print(result)