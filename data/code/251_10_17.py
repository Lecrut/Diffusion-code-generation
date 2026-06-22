MAX_VALUE = float('-inf')

def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        return None
    largest = MAX_VALUE
    for number in numbers:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    sample_data = [42, 10, 99, 5, 123, 78]
    result = determine_the_largest_number_present_calculate(sample_data)
    print(result)