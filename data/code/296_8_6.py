class RatioManipulator:
    @staticmethod
    def change_ratio(ratio_string, factor):
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Invalid ratio format. Expected 'a:b'.")
            num_str, den_str = parts
            numerator = float(num_str)
            denominator = float(den_str)
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            new_numerator = numerator * factor
            new_denominator = denominator * factor
            return f"{new_numerator}:{new_denominator}"
        except ValueError as e:
            return f"Error processing ratio string: {e}"
        except ZeroDivisionError:
            return "Error: Division by zero encountered."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    print(RatioManipulator.change_ratio('4:5', 2.0))
    print(RatioManipulator.change_ratio('10:3', 0.5))
    print(RatioManipulator.change_ratio('7:2', 1.5))
    print(RatioManipulator.change_ratio('1:1', 3.14159))
    print(RatioManipulator.change_ratio('8:10', -1.5))
    print(RatioManipulator.change_ratio('2:0', 10.0))