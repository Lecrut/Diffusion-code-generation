def is_strictly_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    sample_values = [(5, 3), (2, 4), (7, 7)]
    for num1, num2 in sample_values:
        result = is_strictly_greater(num1, num2)
        print(result)