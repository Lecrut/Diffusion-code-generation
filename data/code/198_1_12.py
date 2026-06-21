def find_smallest_element(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [3.5, 1.2, -4.8, 7.6, 0.0, -2.3]
    print(find_smallest_element(sample_values))