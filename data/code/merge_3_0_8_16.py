def convert_length(length_cm):
    """
    Converts a length given in centimeters to miles and kilometers.
    
    Parameters:
        length_cm (float or int): Length value in centimeters.
        
    Returns:
        tuple: A tuple containing the converted lengths rounded to two decimal places,
               as (miles, kilometers).
    """
    # Conversion factors
    meters_per_km = 100
    cm_to_meters = 0.01
    
    length_in_meters = length_cm * cm_to_meters
    length_in_kilometers = length_in_meters / meters_per_km
    
    inches_per_foot = 12
    feet_per_yard = 3
    yards_per_chain = 66 # A chain is a standard unit often used in land surveying, but here we calculate directly from cm to miles.
    miles_conversion_factor_cm_to_mi = (0.0254 * inches_per_foot / feet_per_yard) / length_in_meters # This approach above was flawed logic for direct conversion factor
    
    # Correct Calculation: 1 mile = 160934.4 cm exactly based on standard definition
    miles = length_cm / 160934.4
    
    kilometers = length_in_kilometers

    return round(miles, 2), round(kilometers, 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes as per task requirements
    test_values = [160934.4, 5000, -100]

    print("Sample Input-Output Test:")
    
    try:
        for length in test_values:
            miles_result, km_result = convert_length(length)
            
            # Output formatting to two decimal places as requested
            output_miles = f"{miles_result:.2f}"
            output_km = f"{km_result:.2f}"

            print(f"Input (cm): {length}")
            print(f"Miles: {output_miles}, Kilometers: {output_km}\n")
            
    except Exception as e:
        print(f"An error occurred during processing: {e}")