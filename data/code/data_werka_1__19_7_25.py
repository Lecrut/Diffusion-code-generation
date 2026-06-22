def is_strictly_greater(num1, num2):
    try:
        return int(num1) > int(num2)
    except ValueError:
        return "Invalid input: Both inputs must be integers."

if __name__ == '__main__':
    sample_num1 = '10'
    sample_num2 = '5'
    result = is_strictly_greater(sample_num1, sample_num2)
    print(result)

    sample_num3 = 'abc'
    sample_num4 = 'def'
    result2 = is_strictly_greater(sample_num3, sample_num4)
    print(result2)