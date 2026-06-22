def sort_and_print(numbers):
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        print(number)

if __name__ == '__main__':
    sample_list = [51, 47, 33, 25, 10]
    sort_and_print(sample_list)