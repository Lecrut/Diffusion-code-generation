class DistanceConverter:
    def __init__(self):
        self.miles_to_km_factor = 1.60934
    
    def convert_miles_to_kilometers(self, value) -> float | None:
        """Convert distance from miles to kilometers."""
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Input must be a numeric type.")
            
            result = value * self.miles_to_km_factor
            return round(result, 6) # Round for efficiency and standard precision output
        except Exception as e:
            print(f"Error during conversion: {e}")
            return None
    
    def convert_kilometers_to_miles(self, value) -> float | None:
        """Convert distance from kilometers to miles."""
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Input must be a numeric type.")
            
            result = value / self.miles_to_km_factor
            return round(result, 6)
        except Exception as e:
            print(f"Error during conversion: {e}")
            return None

if __name__ == '__main__':
    # Sample values run without user input or external dependencies
    
    converter = DistanceConverter()
    
    # Test cases with hard-coded sample values
    test_cases_miles = [10, 5.5, -3]
    test_cases_km = [8.967240, 10 * converter.miles_to_km_factor + 1, "invalid"]

    print("--- Miles to Kilometers ---")
    
    for val in test_cases_miles:
        result = converter.convert_miles_to_kilometers(val)
        if isinstance(result, float):
            print(f"{val} miles = {result} kilometers")
        else:
            print("Conversion failed.")

    print("\n--- Kilometers to Miles ---")
    
    for val in test_cases_km:
        result = converter.convert_kilometers_to_miles(val)
        if isinstance(result, float):
            # Note: "invalid" string will trigger type error and return None/Print Error message inside method logic handled by class but here we catch at runtime or let it fail as per strict validation requirement. 
            # The prompt requires handling non-numeric input inside the class method which returns None on failure, not necessarily crashing the script if called directly in a robust way, BUT since this is run via `if __name__`, and "invalid" is passed to convert_kilometers_to_miles:
            pass
        
        print(f"{val} kilometers = {result:.6f} miles")

    # Explicit validation check for non-numeric string input within the class logic as requested by task constraints.
    # Re-running specific error case demonstration inside main block without crashing script flow if handled gracefully, 
    # however since convert methods return None on internal failure but print an error message:
    
    try:
        bad_input = "30"
        res_miles_to_km = converter.convert_miles_to_kilometers(bad_input)
        print(f"\nTesting non-numeric input '30': Result is {res_miles_to_km}")
    except TypeError as te:
        # This specific try-except block wraps the method call to prevent uncaught exceptions if we wanted silent fail, 
        # but per instructions "handle input validation", usually implies raising or returning error. The class returns None and prints.
        pass