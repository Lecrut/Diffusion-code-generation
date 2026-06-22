def find_smallest_element(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [4, 2, 9, 1, 5, 6]
    print(find_smallest_element(sample_values))