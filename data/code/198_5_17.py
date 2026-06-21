def find_absolute_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_absolute_minimum(sample_values))