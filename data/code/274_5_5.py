def print_sorted(numbers):
    numbers.sort()
    for number in numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 7]
    print_sorted(sample_values)