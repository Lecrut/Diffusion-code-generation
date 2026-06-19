def filter_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

if __name__ == '__main__':
    sample_list = [10, 23, 45, 68, 79, 82]
    result = filter_odd_numbers(sample_list)
    print(result)