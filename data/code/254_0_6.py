def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_list = [7, 3, 9, 2, 5, 8, 4, 6, 1]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)