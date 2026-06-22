def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    min_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
    
    return min_value

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_minimum(sample_numbers)
    print(result)