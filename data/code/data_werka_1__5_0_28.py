def calculate_difference(length1, length2):
    try:
        num1 = float(length1)
        num2 = float(length2)
        return abs(num1 - num2)
    except ValueError:
        return "Invalid input: Please enter numeric values."

if __name__ == '__main__':
    sample_length1 = '10.5'
    sample_length2 = '4.2'
    difference = calculate_difference(sample_length1, sample_length2)
    print(difference)