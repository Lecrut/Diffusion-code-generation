def divide_two_numbers(dividend, divisor):
    if divisor == 0:
        return None, "Error: Division by zero is not allowed."
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    num1 = 25
    num2 = 4
    result1, message1 = divide_two_numbers(num1, num2)
    print(f"Result of {num1} // {num2}: {result1}, Remainder: {message1}")

    num3 = 10
    num4 = 3
    result2, message2 = divide_two_numbers(num3, num4)
    print(f"Result of {num3} // {num4}: {result2}, Remainder: {message2}")