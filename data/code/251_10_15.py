MAX_NUMBER = 9999

def determine_the_largest_number_present_calculate(numbers):
    return max(numbers)
if __name__ == '__main__':
    sample_numbers = [345, 678, 123, 901]
    largest_number = determine_the_largest_number_present_calculate(sample_numbers)
    print(largest_number)