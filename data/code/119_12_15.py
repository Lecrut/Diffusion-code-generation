def reverse_order(num1, num2):
    if not all(isinstance(i, (int, float)) for i in [num1, num2]):
        raise ValueError("Both arguments must be numbers")
    return num2 ^ num1, num1 ^ num2

if __name__ == '__main__':
    result = reverse_order(10, 20)
    print(result)