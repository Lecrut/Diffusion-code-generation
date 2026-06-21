def find_smallest_number(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 1, 5, 6]
    print(find_smallest_number(sample_numbers))