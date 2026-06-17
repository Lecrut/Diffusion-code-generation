class RatioManipulator:
    @staticmethod
    def change_ratio(ratio_string, factor):
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Invalid ratio format. Use 'a:b'.")
            num = float(parts[0])
            den = float(parts[1])
            if den == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            new_num = num * factor
            new_den = den * factor
            return f"{new_num}:{new_den}"
        except ValueError as e:
            return f"Error processing ratio: {e}"
        except ZeroDivisionError:
            return "Error: Division by zero encountered."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    ratio1 = '4:5'
    factor1 = 2.5
    result1 = RatioManipulator.change_ratio(ratio1, factor1)
    print(f"Original ratio: {ratio1}, Factor: {factor1}")
    print(f"New ratio: {result1}\n")
    ratio2 = '10:3'
    factor2 = 0.5
    result2 = RatioManipulator.change_ratio(ratio2, factor2)
    print(f"Original ratio: {ratio2}, Factor: {factor2}")
    print(f"New ratio: {result2}\n")
    ratio3 = '1:1'
    factor3 = 100.0
    result3 = RatioManipulator.change_ratio(ratio3, factor3)
    print(f"Original ratio: {ratio3}, Factor: {factor3}")
    print(f"New ratio: {result3}\n")
    ratio4 = '7:2'
    factor4 = 1.0 / 3.0
    result4 = RatioManipulator.change_ratio(ratio4, factor4)
    print(f"Original ratio: {ratio4}, Factor: {factor4}")
    print(f"New ratio: {result4}\n")