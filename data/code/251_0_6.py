MAX_VALUE_THRESHOLD = 100

def determine_the_largest_number_present_transform(numbers):
    if not numbers:
        return None
    
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value and number <= MAX_VALUE_THRESHOLD:
            max_value = number
    
    return max_value

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2, 99, 101]
    print(determine_the_largest_number_present_transform(sample_numbers))