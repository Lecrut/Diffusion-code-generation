class RatioManipulator:
    @staticmethod
    def change_ratio(ratio_string, factor):
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Invalid ratio format. Expected 'a:b'.")
            a = float(parts[0])
            b = float(parts[1])
            if a == 0 or b == 0:
                raise ZeroDivisionError("Ratio components cannot be zero.")
            new_a = a * factor
            new_b = b * factor
            return f"{new_a:.6f}:{new_b:.6f}"
        except ValueError as e:
            raise ValueError(f"Error parsing ratio string '{ratio_string}': {e}")
        except ZeroDivisionError:
            raise ValueError("Cannot perform multiplication when a component is zero.")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    print(RatioManipulator.change_ratio('4:5', 2.0))
    print(RatioManipulator.change_ratio('10:3', 0.5))
    print(RatioManipulator.change_ratio('1:1', 1.0000000000000001))
    try:
        RatioManipulator.change_ratio('2:0', 1.5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        RatioManipulator.change_ratio('abc:5', 2.0)
    except ValueError as e:
        print(f"Error caught: {e}")