def find_smallest_value(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_smallest_value(sample_values))