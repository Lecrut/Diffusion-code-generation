def find_max_element(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    
    return max_value

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max_element(sample_values))