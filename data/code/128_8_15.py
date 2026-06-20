def check_negativity(num):
    return num < 0
if __name__ == '__main__':
    test_numbers = [-3, 7, -15, 2, -9, 0]
    negative_nums = [num for num in test_numbers if check_negativity(num)]
    print(negative_nums)