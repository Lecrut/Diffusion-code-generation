def find_largest(numbers):
    return max([n for n in numbers])

if __name__ == '__main__':
    sample_numbers = [10, 45, 3, 89, 22, 56, 99, 4, 77]
    largest_value = find_largest(sample_numbers)
    print(largest_value)