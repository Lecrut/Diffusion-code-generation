class RatioManipulator:
    @staticmethod
    def change_ratio(ratio_string, factor):
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Invalid ratio format. Use 'a:b'.")
            a = float(parts[0])
            b = float(parts[1])
            if a == 0 or b == 0:
                raise ZeroDivisionError("Ratio components cannot be zero.")
            new_a = a * factor
            new_b = b * factor
            return f"{new_a:.6f}:{new_b:.6f}"
        except ValueError as e:
            return f"Error processing ratio string: {e}"
        except ZeroDivisionError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    print(RatioManipulator.change_ratio('4:5', 2.0))
    print(RatioManipulator.change_ratio('10:3', 0.5))
    print(RatioManipulator.change_ratio('1:1', 1.000000000000001))
    print(RatioManipulator.change_ratio('7:2', 3.333333333333333))
    print(RatioManipulator.change_ratio('0:5', 10.0))
    print(RatioManipulator.change_ratio('5:0', 2.0))