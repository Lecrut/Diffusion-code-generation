def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        sample_num1 = 10
        sample_num2 = 5
        result = is_strictly_greater(sample_num1, sample_num2)
        print(result)
        sample_num1 = 3
        sample_num2 = 7
        result = is_strictly_greater(sample_num1, sample_num2)
        print(result)
    except ValueError as e:
        print(e)