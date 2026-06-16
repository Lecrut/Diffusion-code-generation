class RatioManipulator:
    @staticmethod
    def change_ratio(ratio_string, factor):
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Invalid ratio format. Expected 'a:b'.")
            num = float(parts[0])
            den = float(parts[1])
            if den == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            new_num = num * factor
            new_den = den * factor
            return f"{new_num}:{new_den}"
        except ValueError as e:
            raise ValueError(f"Error processing ratio string '{ratio_string}': {e}")
        except ZeroDivisionError:
            raise ValueError("Operation resulted in division by zero.")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    print(RatioManipulator.change_ratio('4:5', 2.0))
    print(RatioManipulator.change_ratio('10:3', 0.5))
    print(RatioManipulator.change_ratio('1:1', 1.1))
    print(RatioManipulator.change_ratio('7:2', 3.0))
    try:
        RatioManipulator.change_ratio('5:0', 2.0)
    except ValueError as e:
        print(f"Error caught: {e}")