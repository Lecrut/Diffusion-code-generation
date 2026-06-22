def calculate_range(numbers):
    if not numbers:
        return 0
    
    current_min = current_max = numbers[0]
    
    for number in numbers[1:]:
        if number < current_min:
            current_min = number
        elif number > current_max:
            current_max = number
    
    return current_max - current_min

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    result = calculate_range(sample_list)
    print(result)