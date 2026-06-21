def find_smallest_element(numbers):
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 0.577, 1.618, -1.414]
    print(find_smallest_element(sample_numbers))