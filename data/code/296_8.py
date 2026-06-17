class RatioManipulator:
    @staticmethod
    def manipulate_ratio(ratio_string, factor):
        try:
            parts = ratio_string.split(':')
            if len(parts) != 2:
                raise ValueError("Invalid ratio format. Expected 'a:b'.")
            original_a = float(parts[0])
            original_b = float(parts[1])
            if original_a == 0 or original_b == 0:
                raise ZeroDivisionError("Ratio components cannot be zero.")
            new_a = original_a * factor
            new_b = original_b * factor
            return new_a, new_b
        except ValueError as e:
            raise ValueError(f"Error parsing ratio string '{ratio_string}': {e}")
        except ZeroDivisionError:
            raise ValueError("Cannot manipulate ratios involving zero.")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    print("--- Test Case 1: Simple Multiplication ---")
    try:
        ratio_str = '4:5'
        factor = 2.0
        result_a, result_b = RatioManipulator.manipulate_ratio(ratio_str, factor)
        print(f"Original ratio: {ratio_str}")
        print(f"Factor: {factor}")
        print(f"New ratio: {result_a}:{result_b}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Multiplication by Decimal ---")
    try:
        ratio_str = '10:3'
        factor = 0.5
        result_a, result_b = RatioManipulator.manipulate_ratio(ratio_str, factor)
        print(f"Original ratio: {ratio_str}")
        print(f"Factor: {factor}")
        print(f"New ratio: {result_a}:{result_b}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Multiplication by Negative Factor ---")
    try:
        ratio_str = '2:7'
        factor = -1.5
        result_a, result_b = RatioManipulator.manipulate_ratio(ratio_str, factor)
        print(f"Original ratio: {ratio_str}")
        print(f"Factor: {factor}")
        print(f"New ratio: {result_a}:{result_b}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Handling Floating Point Inaccuracy (Subtraction Check) ---")
    try:
        ratio_str = '10:1'
        factor = 3.333333333333333                        
        result_a, result_b = RatioManipulator.manipulate_ratio(ratio_str, factor)
        print(f"Original ratio: {ratio_str}")
        print(f"Factor: {factor}")
        print(f"New ratio (A): {result_a}")
        print(f"New ratio (B): {result_b}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Error Handling (Invalid Format) ---")
    try:
        RatioManipulator.manipulate_ratio('4/5', 2)
    except ValueError as e:
        print(f"Caught expected error for invalid format: {e}")
    print("\n--- Test Case 6: Error Handling (Zero Component) ---")
    try:
        RatioManipulator.manipulate_ratio('0:5', 2)
    except ValueError as e:
        print(f"Caught expected error for zero component: {e}")