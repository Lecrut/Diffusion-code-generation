LARGEST_NUMBER = float('-inf')

def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        return LARGEST_NUMBER
    
    largest = max(numbers)
    
    return largest

if __name__ == '__main__':
    sample_data = [42, 10, 99, 5, 123, 78]
    result = determine_the_largest_number_present_calculate(sample_data)
    print(result)