def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    print(find_smallest(sample_values))