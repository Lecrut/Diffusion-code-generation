def bitwise_and(num1: int, num2: int) -> int:
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError('Inputs must be integers')
    result = num1 & num2
    return result
if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(bitwise_and(num1, num2))