def find_smallest_number(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    
    return smallest

if __name__ == '__main__':
    sample_data = [7, 3, 9, 2, 5]
    try:
        print(find_smallest_number(sample_data))
    except ValueError as e:
        print(e)