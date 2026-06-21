def find_smallest_element(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 4.8, -2.1, 0.0]
    print(find_smallest_element(sample_numbers))