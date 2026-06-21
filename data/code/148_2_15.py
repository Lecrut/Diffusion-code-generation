def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

if __name__ == '__main__':
    sample_data = [10, 5, 20, 15, 30]
    try:
        result = find_largest_element(sample_data)
        print(result)
    except ValueError as e:
        print(e)