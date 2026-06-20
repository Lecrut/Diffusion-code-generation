SUBTRACTION_THRESHOLD = 100

def subtract_amounts(num1, num2):
    if abs(num1 - num2) < SUBTRACTION_THRESHOLD:
        return num1 - num2
    else:
        raise ValueError("The difference between the numbers is too large.")

if __name__ == '__main__':
    result = subtract_amounts(50, 30)
    print(result)