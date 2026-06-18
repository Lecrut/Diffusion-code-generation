import math

class DistanceConverter:
    """A class to convert distances between miles and kilometers."""

    # Conversion factor: 1 mile = 1.609344 kilometers (exact definition)
    MILES_TO_KM_FACTOR = 1.609344

    def __init__(self):
        pass

    def validate_input(self, value):
        """
        Validates that the input is a numeric type and returns it as a float.
        
        Args:
            value (any): The value to be validated.
            
        Returns:
            float: The converted float value if valid.
            
        Raises:
            TypeError: If the input is not an instance of int or float, 
                      or if it cannot be represented as a finite number.
        """
        if isinstance(value, (int, float)):
            # Check for infinity and NaN to ensure mathematical soundness in calculations
            if math.isnan(float(value)) or math.isinf(float(value)):
                raise ValueError("Input value must be a valid finite number.")
            return float(value)
        
        try:
            num = float(value)
            if math.isnan(num) or math.isinf(num):
                raise ValueError("Input value must be a valid finite number.")
            return num
        except (ValueError, TypeError):
            # Covers cases where input is not numeric and cannot be converted to float
            raise TypeError(f"Invalid type for distance: {type(value).__name__}. Expected int or float.")

    def miles_to_kilometers(self, value):
        """
        Converts a distance from miles to kilometers.
        
        Args:
            value (int | float): The distance in miles. Must be numeric and non-negative 
                                for physical distances, though negative mathematically converts correctly.
            
        Returns:
            float: The equivalent distance in kilometers.
            
        Raises:
            TypeError: If the input is not a valid number.
        """
        validated_value = self.validate_input(value)
        return validated_value * self.MILES_TO_KM_FACTOR

    def kilometers_to_miles(self, value):
        """
        Converts a distance from kilometers to miles.
        
        Args:
            value (int | float): The distance in kilometers. Must be numeric and non-negative 
                                for physical distances, though negative mathematically converts correctly.
            
        Returns:
            float: The equivalent distance in miles.
            
        Raises:
            TypeError: If the input is not a valid number.
        """
        validated_value = self.validate_input(value)
        return validated_value / self.MILES_TO_KM_FACTOR

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    converter = DistanceConverter()

    # Sample 1: Convert standard distance (5 miles)
    try:
        result_km = converter.miles_to_kilometers(5.0)
        print(f"5.0 miles is equal to {result_km:.2f} kilometers.")
    except Exception as e:
        print(f"Error during conversion: {e}")

    # Sample 2: Convert standard distance (10 km) back to miles
    try:
        result_mi = converter.kilometers_to_miles(10.0)
        print(f"10.0 kilometers is equal to {result_mi:.5f} miles.")
    except Exception as e:
        print(f"Error during conversion: {e}")

    # Sample 3: Test input validation with non-numeric value (string 'abc')
    try:
        result = converter.miles_to_kilometers("invalid")
        print(f"Converted invalid string to float: {result}")
    except TypeError as e:
        print(f"Caught expected type error for non-numeric input: {e}")

    # Sample 4: Test input validation with integer (10)
    try:
        result = converter.miles_to_kilometers(10)
        print(f"Integer input 10 miles is equal to {result:.2f} kilometers.")
    except Exception as e:
        print(f"Unexpected error for valid int input: {e}")

    # Sample 5: Test edge case with zero distance
    try:
        result = converter.miles_to_kilometers(0)
        print(f"Zero miles is equal to {result:.2f} kilometers.")
    except Exception as e:
        print(f"Error during conversion of zero: {e}")

    # Sample 6: Test with negative value (mathematically valid, physically odd but handled correctly by logic)
    try:
        result = converter.miles_to_kilometers(-10.5)
        print(f"-10.5 miles is equal to {result:.2f} kilometers.")
    except Exception as e:
        print(f"Error during conversion of negative value: {e}")

    # Sample 7: Test input validation with float containing decimal precision
    try:
        result = converter.miles_to_kilometers(1.609344)
        print(f"1.609344 miles is equal to {result:.5f} kilometers.")
    except Exception as e:
        print(f"Error during conversion of precise float input: {e}")

    # Sample 8: Test with large value (simulating a long distance)
    try:
        result = converter.miles_to_kilometers(1000.0)
        print(f"1000 miles is equal to {result:.2f} kilometers.")
    except Exception as e:
        print(f"Error during conversion of large value: {e}")

    # Sample 9: Test input validation with None type
    try:
        result = converter.miles_to_kilometers(None)
        print(f"Converted None to float: {result}")
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for None input: {e}")

    # Sample 10: Test with a list instead of number
    try:
        result = converter.miles_to_kilometers([5])
        print(f"Converted list to float: {result}")
    except TypeError as e:
        print(f"Caught expected type error for list input: {e}")

    # Sample 11: Test with a boolean (treated as numeric in Python, but explicitly checking behavior)
    try:
        result = converter.miles_to_kilometers(True)
        print(f"Boolean True converted to float and miles->km is equal to {result:.5f} kilometers.")
        
        # Verify False case too for completeness of logic check
        result_false = converter.kilometers_to_miles(False)
        print(f"Boolean False in km conversion resulted in: {result_false}")
    except Exception as e:
        print(f"Unexpected error with boolean inputs: {e}")

    # Sample 12: Test input validation with complex number (if supported by float constructor, usually it fails gracefully or raises)
    try:
        result = converter.miles_to_kilometers(5+3j)
        print(f"Converted complex to float: {result}")
    except TypeError as e:
        # Complex numbers are not instances of int/float and fail the first check, 
        # but let's see if float() handles it. It usually raises ValueError or similar depending on impl.
        # In standard Python 3, float(complex) is not allowed directly without error in some contexts or returns real part? 
        # Actually float(5+3j) raises TypeError: complex argument required for conversion to int/float? No, it's different.
        # Let's stick to the defined validate_input which checks isinstance first then tries convert.
        print(f"Caught expected error handling attempt with complex number type: {e}")

    # Sample 13: Test input validation with NaN explicitly created via math library if possible in scope (requires import)
    try:
        import math as mth
        nan_val = float('nan')
        result = converter.miles_to_kilometers(nan_val)
        print(f"Converted NaN to km: {result}") # Should ideally raise ValueError based on validation logic
    except Exception as e:
        if "must be a valid finite number" in str(e):
            print("Caught expected error for NaN input.")
        else:
            print(f"Different exception occurred with NaN: {e}")

    # Sample 14: Test infinity explicitly created via math library