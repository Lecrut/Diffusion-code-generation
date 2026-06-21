def filter_odd(numbers):
    return [x for x in numbers if x % 2 != 0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odd(sample_list)
    print(odd_numbers)