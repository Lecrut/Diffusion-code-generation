def check_number(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    test_numbers = [5, -3, 0]
    for number in test_numbers:
        status = check_number(number)
        print(f'The number {number} is {status}')