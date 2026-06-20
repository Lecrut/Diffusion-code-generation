def reverse_order(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return [num2, num1]

if __name__ == '__main__':
    result = reverse_order(10, 20)
    print(result)
    result2 = reverse_order(5.5, 8.2)
    print(result2)