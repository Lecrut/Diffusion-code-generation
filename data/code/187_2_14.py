def find_largest_element(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    
    return largest

if __name__ == '__main__':
    sample_data = [42, 7, 3, 5, 99, 1, 100, 65]
    result = find_largest_element(sample_data)
    print(result)