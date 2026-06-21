def find_smallest_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    
    return smallest

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_smallest_element(sample_values))