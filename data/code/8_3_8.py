def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given length and width."""
    try:
        return length * width
    except Exception as e:
        print(f"Error during calculation: {e}")
        raise

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements
    length = 5.0
    width = 3.5

    try:
        area_result = calculate_area(length, width)
        print(f"Rectangle dimensions (length={length}, width={width})")
        print(f"Calculated Area: {area_result}")
        
        # Demonstrate ValueError handling with simulated non-numeric inputs in a clean way
        def handle_non_numeric_input():
            """Simulates input validation without using actual stdin."""
            test_values = ['a', 10, 'invalid']
            
            for val in test_values:
                try:
                    area_val = calculate_area(val, width)
                    print(f"Success with {val}: Area is {area_val}")
                except ValueError as ve:
                    print(f"ValueError handled correctly for input '{val}': Input was not numeric.")
                except TypeError as te:
                     # Catch cases where the try block fails before multiplication (e.g., 'a' * float) 
                     if isinstance(val, str):
                        raise f"{type(val).__name__}" from None
        
        handle_non_numeric_input()

    except ValueError as ve:
        print(f"Caught specific non-numeric input error: {ve}")