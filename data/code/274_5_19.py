def print_sorted_numbers(numbers):
    numbers.sort()
    for number in numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [10, 25, 33, 47, 51]
    print_sorted_numbers(sample_values)