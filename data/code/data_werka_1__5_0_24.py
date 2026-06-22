def calculate_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return abs(num1 - num2)
    except ValueError:
        return 'Error: Both inputs must be numeric.'
if __name__ == '__main__':
    length_a = '15.5'
    length_b = '10.2'
    result = calculate_difference(length_a, length_b)
    print(result)