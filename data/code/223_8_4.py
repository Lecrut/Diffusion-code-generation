def find_largest_number(numbers):
    numbers.sort(reverse=True)
    return numbers[0]

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    largest_number = find_largest_number(sample_numbers)
    print(largest_number)