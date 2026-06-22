def print_sorted_numbers(numbers):
    numbers.sort()
    for number in numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    print_sorted_numbers(sample_values)