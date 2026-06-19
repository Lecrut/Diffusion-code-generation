def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    sample_sides = [5, -3, "invalid"]
    
    for i, side in enumerate(sample_sides):
        print(f"\n--- Processing Side Length Index {i + 1} ---")
        
        # Attempt to calculate area using the provided value (which may be a string)
        try:
            # If input is not numeric, Python will raise TypeError when passed to **2 or checked in calculation logic.
            # However, to demonstrate robust error handling as per general best practices for such tasks, 
            # we assume here that valid inputs are floats/ints and invalid ones trigger appropriate errors.
            
            if side == "invalid":
                print("Input detected as non-numeric string.")
                
                try:
                    area = float(side) ** 2
                    print(f"Calculated Area (treated as number): {area}")
                except ValueError:
                    print("Error: Cannot convert input to a numeric value for calculation.")
            else:
                # Calculate the actual area based on integer or float inputs like -3 and 5.
                try:
                    calculated_area = calculate_square_area(side)
                    
                    if isinstance(calculated_area, int):
                        print(f"Calculated Area (integer result): {calculated_area}")
                    else:
                        # Using the logic that area is a float but side could be integer in Python 3 automatically promotes type. 
                        # The function returns square so it might return int if input was int and square results in int math.
                        print(f"Calculated Area (float result): {calculated_area}")

                except ValueError as ve:
                    print(f"Error during calculation due to value constraint: {ve}.")
                    
        except Exception as e:
            # This catches unexpected errors unrelated to the specific logic flow defined above.
            if "negative" in str(e).lower():
                print("Specific error detected regarding side length constraints.")
                
    print("\n--- Execution Complete ---")