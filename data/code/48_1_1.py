def find_largest(numbers):
    return max([n for n in numbers])

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_largest(sample_numbers))