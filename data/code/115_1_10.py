class IntegerDivider:
    def divide(self, a, b):
        if b == 0:
            return None, "Error: Division by zero is not allowed."
        quotient = a // b
        remainder = a % b
        return quotient, remainder

if __name__ == '__main__':
    divider = IntegerDivider()
    result1 = divider.divide(10, 2)
    print(f"Result of 10 / 2: Quotient={result1[0]}, Remainder={result1[1]}")
    
    result2 = divider.divide(15, 0)
    print(f"Result of 15 / 0: {result2}")
    
    result3 = divider.divide(-20, 5)
    print(f"Result of -20 / 5: Quotient={result3[0]}, Remainder={result3[1]}")