def print_even_numbers(numbers):
    even_nums = [num for num in numbers if num % 2 == 0]
    for num in even_nums:
        print(num)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_even_numbers(sample_list)