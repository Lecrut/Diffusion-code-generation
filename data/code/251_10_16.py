MAX_NUMBER = 999

def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    largest_number = numbers[0]
    for number in numbers[1:]:
        if number > largest_number:
            largest_number = number
    
    return largest_number

if __name__ == '__main__':
    sample_numbers = [42, 10, 99, 5, 123, 78, MAX_NUMBER]
    try:
        result = determine_the_largest_number_present_calculate(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)