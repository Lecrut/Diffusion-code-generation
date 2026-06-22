def print_sorted_numbers(numbers):
    numbers.sort()
    for number in numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [5, 2, 9, 1, 5, 6]
    print_sorted_numbers(sample_values)