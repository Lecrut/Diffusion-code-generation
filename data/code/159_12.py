def print_odd_numbers(numbers):
    for number in numbers:
        if number % 2 != 0:
            print(number)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_odd_numbers(sample_list)