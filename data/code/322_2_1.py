class QuantityDivider:
    def divide(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Cannot divide by zero")
        return numerator / denominator
if __name__ == '__main__':
    divider = QuantityDivider()
    try:
        result1 = divider.divide(10, 2)
        print(f"10 divided by 2 is: {result1}")
        result2 = divider.divide(15, 3)
        print(f"15 divided by 3 is: {result2}")
        result3 = divider.divide(7, 0)
    except ValueError as e:
        print(f"Error caught: {e}")