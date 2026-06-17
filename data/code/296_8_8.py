class RatioManipulator:
    @staticmethod
    def change_ratio_by_factor(ratio_string, factor):
        if ':' not in ratio_string:
            raise ValueError("Invalid ratio format. Expected 'a:b'.")
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Ratio string must contain exactly one colon.")
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            if a == 0 or b == 0:
                raise ZeroDivisionError("Ratio components cannot be zero.")
            new_a = a * factor
            new_b = b * factor
            return f"{new_a:.6f}:{new_b:.6f}"
        except ValueError as e:
            raise ValueError(f"Invalid number format in ratio string: {ratio_string}. Details: {e}")
        except ZeroDivisionError:
            raise ValueError("Cannot scale a zero ratio.")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    print(RatioManipulator.change_ratio_by_factor('4:5', 2.5))
    print(RatioManipulator.change_ratio_by_factor('10:3', 0.5))
    print(RatioManipulator.change_ratio_by_factor('1:1', 100.0))
    try:
        RatioManipulator.change_ratio_by_factor('2:0', 1.0)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        RatioManipulator.change_ratio_by_factor('abc:5', 2.0)
    except ValueError as e:
        print(f"Error caught: {e}")