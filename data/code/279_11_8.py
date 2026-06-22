def reverse_and_print(numbers):
    reversed_numbers = numbers[::-1]
    for number in reversed_numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [5, 4, 3, 2, 1]
    reverse_and_print(sample_values)