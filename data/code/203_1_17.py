def is_strictly_greater(num1: int, num2: int) -> bool:
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError('Both arguments must be integers')
    return num1 > num2
if __name__ == '__main__':
    sample_num1 = 5
    sample_num2 = 3
    result = is_strictly_greater(sample_num1, sample_num2)
    print(result)