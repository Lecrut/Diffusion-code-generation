MAX_NUMBERS = {'A': 100, 'B': 200, 'C': 300}

def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest
if __name__ == '__main__':
    sample_numbers = [42, 10, 99, 5, 123, 78]
    result = determine_the_largest_number_present_calculate(sample_numbers)
    print(result)