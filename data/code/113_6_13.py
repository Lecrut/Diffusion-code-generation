def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    num1 = 100
    num2 = 45
    result1 = subtract_numbers(num1, num2)
    print(f"Result of {num1} - {num2}: {result1}")

    num3 = 50
    num4 = 150
    try:
        result2 = subtract_numbers(num3, num4)
    except ValueError as e:
        print(f"Error: {e}")