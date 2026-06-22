def find_largest(numbers):
    return max([num for num in numbers])

if __name__ == '__main__':
    sample_numbers = [10, 25, 3, 99, 42, 0, -5, 100]
    result = find_largest(sample_numbers)
    print(result)