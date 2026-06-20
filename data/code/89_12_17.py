def bitwise_and(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Both inputs must be integers")
    return num1 & num2

if __name__ == '__main__':
    print(bitwise_and(10, 5))