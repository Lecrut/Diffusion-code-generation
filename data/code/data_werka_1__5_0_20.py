def calculate_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        difference = abs(num1 - num2)
        return difference
    except ValueError:
        return 'Error: Both inputs must be numeric.'
if __name__ == '__main__':
    length1 = '10.5'
    length2 = '3.2'
    result = calculate_difference(length1, length2)
    print(result)