def check_negativity(number):
    return number < 0

if __name__ == '__main__':
    test_numbers = [15, -3, 42, -7, 0]
    negative_numbers = [num for num in test_numbers if check_negativity(num)]
    print(negative_numbers)