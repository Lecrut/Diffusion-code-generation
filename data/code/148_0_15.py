def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    
    return largest

if __name__ == '__main__':
    sample_list = [3, 7, 2, 8, 5]
    largest = find_largest_element(sample_list)
    print(largest)