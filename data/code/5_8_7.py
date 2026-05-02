if __name__ == '__main__':
    length1 = 15.5
    length2 = 22.0
    num1 = float(length1)
    num2 = float(length2)
    absolute_difference = abs(num1 - num2)
    if num1 != 0 and num2 != 0:
        percentage_difference = (absolute_difference / ((num1 + num2) / 2)) * 100
    else:
        percentage_difference = float('inf') if absolute_difference != 0 else 0.0
    print("Length 1:", length1)
    print("Length 2:", length2)
    print("---------------------------------")
    print("Absolute Difference:", absolute_difference)
    print("Percentage Difference:", percentage_difference)