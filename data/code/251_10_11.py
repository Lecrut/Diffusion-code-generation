NUMBERS = {'sample1': [42, 10, 99, 5, 123, 78], 'sample2': [10, 5, 42, 99, 3, 78], 'sample3': [42, 10, 99, 5, 33], 'sample4': [10, 5, 20, 8, 15]}

def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        raise ValueError('Input list is empty')
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    try:
        print(determine_the_largest_number_present_calculate(NUMBERS['sample1']))
        print(determine_the_largest_number_present_calculate(NUMBERS['sample2']))
        print(determine_the_largest_number_present_calculate(NUMBERS['sample3']))
        print(determine_the_largest_number_present_calculate(NUMBERS['sample4']))
    except ValueError as e:
        print(e)