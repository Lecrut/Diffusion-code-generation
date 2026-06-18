def convert_to_kilograms(weight_list):
    """
    Converts a list of weight measurements to kilograms, handling various units.
    
    Supported units: 'kg', 'g', 'mg', 'lb', 'oz'.
    If an invalid unit or non-numeric value is encountered, the function skips that item 
    and continues processing others without raising an exception for the entire list.
    
    Args:
        weight_list (list): A list of tuples containing a numeric weight value and its string unit.
        
    Returns:
        float: The total sum converted to kilograms. If no valid inputs are found, returns 0.0.
    """
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.45359237,
        'oz': 0.028349523125
    }

    total_kg = 0.0
    
    for item in weight_list:
        try:
            value_str, unit_str = str(item) if isinstance(item, (str,)) else f"{item}"
            
            # Attempt to parse the numeric part and the string part separately if it's a tuple or similar
            if isinstance(item, tuple):
                val_part, unit_part = item
                
                try:
                    value = float(val_part)
                except ValueError:
                    continue  # Skip invalid numbers
                    
                unit_lower = str(unit_part).strip().lower()
                
                if unit_lower not in conversion_factors:
                    continue  # Skip unsupported units

                total_kg += value * conversion_factors[unit_lower]
            else:
                raise TypeError("Each item must be a tuple (value, unit)")
        except Exception:
            continue
            
    return round(total_kg, 6)

if __name__ == '__main__':
    # Hard-coded sample values with various units and potential errors to test gracefully
    samples = [
        ("10", "kg"),           # Valid kg
        (5000, "g"),            # Valid g
        ("2.5 lb", None),       # Invalid tuple structure for parsing above logic but handled by string check below if needed; 
                                # Let's adjust sample to match expected input format better based on docstring assumption of tuples or strings
                                # Re-evaluating: The function expects a list where items can be parsed as (value, unit)
                                # Or potentially just strings like "10 kg". Let's support both for robustness.
    ]

    # Revised sample block to strictly follow the logic that parses value and unit from each item
    # Assuming input format: [("10", "kg"), ("5000", "g")] or ["10 kg"] if string is passed directly? 
    # Based on typical usage, let's assume items are strings like "10 kg" for simplicity in this specific run without complex tuple parsing requirements unless specified.
    # However, the docstring said tuples. Let's stick to a robust parser that handles both or just one clearly defined format.
    
    # Refined samples as per previous logic which expects (value, unit) or similar parseable structure:
    sample_data = [
        ("10", "kg"),           # 10 kg -> 10 * 1
        ("5000", "g"),          # 5000 g -> 5.0 kg
        (2, "lb"),              # 2 lb -> ~0.907... kg
        ("3 oz", None),         # Invalid unit 'None' or missing string for unit part? Let's fix sample to valid tuple with non-string value if needed 
                                # Actually, let's make the function handle strings like "10kg" too just in case, but stick to strict logic.
    ]

    # Corrected Sample Data ensuring all items are parseable as (value_str, unit_str) or similar:
    final_samples = [
        ("15", "kg"),           # 15 kg
        ("2000", "g"),          # 2 kg
        ("4 lb", None),         # This will fail 'None' check. Let's use proper strings.
        (3, "oz")               # 3 oz
    ]

    # Re-writing final_samples to be fully compatible with the logic that expects tuple of two elements where second is string unit:
    valid_final_samples = [
        ("15", "kg"), 
        ("2000", "g"), 
        (4, "lb"),              # 4 lb
        ("3 oz", None)          # This will be skipped because 'None' isn't in conversion_factors. Let's remove or fix.
    ]

    # Final definitive sample list ensuring no errors and variety of units:
    test_input = [
        ("15", "kg"), 
        (2000, "g"), 
        (4, "lb"), 
        (3, "oz")
    ]

    result = convert_to_kilograms(test_input)
    
    print(f"Total weight in kilograms: {result} kg")