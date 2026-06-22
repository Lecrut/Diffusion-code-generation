def find_largest(numbers):
    return max([n for n in numbers])

if __name__ == '__main__':
    sample_numbers = [42, 17, 9, 103, 55, 88, 15, 200, 76]
    result = find_largest(sample_numbers)
    print(result)