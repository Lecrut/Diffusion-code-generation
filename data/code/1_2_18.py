import math

def convert_to_kilograms(measurements):
    """
    Converts a list of weight measurements in various units to kilograms.
    
    Supported units: 'kg', 'g', 'mg', 'lb', 'oz' (case-insensitive).
    Handles errors gracefully by skipping invalid entries and returning the result as a float rounded to 4 decimal places.
    
    Args:
        measurements (list): List of strings representing weight values with unit suffixes.
        
    Returns:
        list[float]: A new list containing weights converted to kilograms, or an empty list if all inputs were invalid/missing.
    """
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.45359237,
        'oz': 0.028349523125
    }

    converted_weights = []

    for item in measurements:
        try:
            if not isinstance(item, str) or not item.strip():
                continue
                
            value_str, unit_str = item.rsplit(None, 1).strip()
            
            # Try to parse the numeric part (supports integers and floats with optional sign/dot)
            parsed_value = float(value_str)
            if math.isnan(parsed_value):
                continue

            unit_lower = unit_str.lower().strip()
            
            if unit_lower not in conversion_factors:
                print(f"Warning: Skipping invalid or unsupported unit '{unit_str}' for value {parsed_value}")
                continue
                
            converted_kg = parsed_value * conversion_factors[unit_lower]
            rounded_result = round(converted_kg, 4)
            converted_weights.append(rounded_result)

        except ValueError as e:
            print(f"Warning: Skipping invalid numeric format '{item}'")
            continue
            
    return converted_weights

if __name__ == '__main__':
    # Hard-coded sample values with various units and potential edge cases
    sample_data = [
        "5 kg",
        "10 g",
        "2.5 mg", 
        "3 lbs 8 oz" if False else None,  # Note: 'lbs' is not strictly supported in this simplified version to avoid complex parsing logic conflicts with simple split; using pure units only for robustness per task constraints unless extended regex used below. Let's stick to the simpler strict unit suffix approach as defined above but adjust sample accordingly or use a more flexible parser if needed. 
        # Re-evaluating: The initial rsplit might fail on "3 lbs 8 oz". To ensure it works without external libraries and handles common cases like '10 lb' (singular/plural) gracefully, let's update the logic slightly to handle pluralization or just stick strictly to what was defined. 
        # Let's refine the sample list to match exactly supported units:
    ]

    # Refined Sample List for strict adherence to initial conversion_factors keys (kg, g, mg, lb, oz) but allowing simple strings like "3 lbs" -> should we support plural? The code currently splits by last space. 'lbs' is not in factors. Let's add 'lb', 'oz' only as singular or allow the user to input standard forms. 
    # Actually, let's update conversion_factors to include common plurals if possible without over-engineering, OR just use simple inputs that fit perfectly.
    # To be safe and robust: I will extend factors slightly in a comment but implement strictly what is needed for guaranteed success on valid inputs like "1 kg", "50 g". 
    # Let's add 'lbs' to the logic dynamically or statically? Static dict lookup fails if key missing. 
    # Decision: Update conversion_factors inside function to include common plurals implicitly by checking substring? No, strict keys are better for clarity unless specified otherwise.
    # I will update the sample list to use only strictly supported singular/plural forms that fit 'lb' and 'oz'. Actually "3 lb" works if key is 'lb'. 
    # Let's just make sure samples work with current code: "5 kg", "10 g". Add a complex one? No, let's keep it simple.
    
    sample_data = [
        "7.2 kg",       # Valid
        "340 g",        # Valid
        "89 mg",        # Valid
        "2 lb",         # Valid if 'lb' is supported (it is) - note: input was 'lbs' in thought, let's use 'lb'. 
        "1.5 oz",       # Valid
        "",             # Empty string test
        "abc kg" ,      # Invalid numeric part
        None            # Null value check if passed as list element (though type hint says str) - handled gracefully? Code checks isinstance(item, str).
    ]

    result = convert_to_kilograms(sample_data)
    
    print("Converted weights in kilograms:")
    for i, weight in enumerate(result):
        print(f"  {i+1}. {weight} kg")