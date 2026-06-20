def determine_number_status(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    test_numbers = [-1, 0, 1]
    for num in test_numbers:
        result = determine_number_status(num)
        print(f'The number {num} is {result}.')