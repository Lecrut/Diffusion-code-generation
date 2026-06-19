def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        input1 = 10
        input2 = 5
        result = is_strictly_greater(input1, input2)
        print(result)
    except ValueError as e:
        print(e)