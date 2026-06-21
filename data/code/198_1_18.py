def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -1.5, 0.0, 2.3]
    print(find_smallest(sample_values))