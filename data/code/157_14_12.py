def find_smallest_value(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5, 1]
    print(find_smallest_value(sample_values))