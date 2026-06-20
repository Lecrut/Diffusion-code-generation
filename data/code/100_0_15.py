def classify_number(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    test_numbers = [2, -1, 0]
    for number in test_numbers:
        result = classify_number(number)
        print(f'The number {number} is {result}.')