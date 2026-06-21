def find_max_element(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [45, 23, 67, 89, 12, 34]
    print(find_max_element(sample_values))