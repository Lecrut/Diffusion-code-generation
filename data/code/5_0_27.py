def calculate_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return abs(num1 - num2)
    except ValueError:
        return None
if __name__ == '__main__':
    length1 = '15.5'
    length2 = '10.3'
    difference = calculate_difference(length1, length2)
    if difference is not None:
        print(f'The difference is: {difference}')
    else:
        print('Error: Non-numeric input provided')