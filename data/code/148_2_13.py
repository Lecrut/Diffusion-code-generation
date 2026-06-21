def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [10, 5, 20, 15, 30]
    try:
        result = find_largest_element(sample_values)
        print(result)
    except ValueError as e:
        print(e)