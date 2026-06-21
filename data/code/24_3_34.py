def extract_negative_numbers(number_list):
    negative_nums = []
    for num in number_list:
        if num < 0:
            negative_nums.append(num)
    return negative_nums

if __name__ == '__main__':
    test_values = [10, -3, 7, -8, 2, -5]
    result = extract_negative_numbers(test_values)
    print(result)