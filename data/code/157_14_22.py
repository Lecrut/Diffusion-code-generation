def find_smallest_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23]
    print(find_smallest_value(sample_values))