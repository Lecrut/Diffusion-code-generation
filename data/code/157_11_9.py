def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 1, 8, 6, 3]
    print(find_smallest(sample_numbers))