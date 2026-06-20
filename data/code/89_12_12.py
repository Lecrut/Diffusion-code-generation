def bitwise_and(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError('Both inputs must be integers.')
    return num1 & num2
if __name__ == '__main__':
    sample_num1 = 170
    sample_num2 = 85
    result = bitwise_and(sample_num1, sample_num2)
    print(result)