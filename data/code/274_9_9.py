def print_unique_elements(numbers):
    unique_numbers = set(numbers)
    for number in unique_numbers:
        print(number)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    print_unique_elements(sample_list)