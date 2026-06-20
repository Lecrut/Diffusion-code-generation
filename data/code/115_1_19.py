class LargeIntegerDivider:
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

if __name__ == '__main__':
    divider = LargeIntegerDivider()
    result1 = divider.divide(10, 2)
    print(f"Quotient of 10 / 2: {result1[0]}, Remainder: {result1[1]}")
    try:
        result2 = divider.divide(15, 0)
        print(f"Quotient of 15 / 0: {result2[0]}, Remainder: {result2[1]}")
    except ValueError as e:
        print(e)