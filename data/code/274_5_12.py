def sort_and_print(numbers):
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        print(number)

if __name__ == '__main__':
    sample_list = [15, 23, 48, 60, 7]
    sort_and_print(sample_list)