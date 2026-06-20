def bitwise_and(num1: int, num2: int) -> int:
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers")
    return num1 & num2

if __name__ == '__main__':
    result = bitwise_and(10, 5)
    print(result)