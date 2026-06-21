def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 12, -3, 7]
    print(find_smallest(sample_values))