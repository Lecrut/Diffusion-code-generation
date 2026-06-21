def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_values = [7, 3, 9, 5, 2, 6]
    print(find_minimum(sample_values))