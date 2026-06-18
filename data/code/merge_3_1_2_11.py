def convert_to_kilograms(measurements):
    """
    Converts a list of weight measurements (in various units) to kilograms.
    
    Supported units: 'kg', 'g' (grams), 'lb' (pounds), 'oz' (ounces).
    Errors are handled gracefully by returning None for invalid entries 
    instead of raising exceptions, which the caller can filter if needed.

    Args:
        measurements (list): List of tuples or lists containing [value, unit_string].
                             Example: [[50, "kg"], [1234], ["lb", 5]] -> Error on invalid format
    
    Returns:
        list: A new list with converted values in kg. Invalid entries are replaced with None.

    Note: This function assumes the input is a list of lists/tuples where 
          each element has at least two parts if it's not already just a number (which defaults to 'g').
    """
    
    def parse_and_convert(entry):
        # Handle direct numeric values as grams by default
        try:
            val = float(entry)
            unit_str = "g"
        except (TypeError, ValueError):
            return None
        
        if isinstance(entry, list) or isinstance(entry, tuple):
            entries_list = list(entry)
            
            # Ensure we have at least a value and optionally a unit string
            try:
                val = float(entries_list[0])
                
                # If there's a second element that looks like a string (unit), use it; else default to 'g'
                if len(entries_list) > 1 and isinstance(entries_list[1], str):
                    unit_str = entries_list[1].strip().lower()
                else:
                    unit_str = "g"
                    
            except (TypeError, ValueError):
                return None

        # Convert based on supported units
        try:
            if not unit_str or unit_str == '':
                unit_str = "g"
                
            elif unit_str in ["kg"]:
                converted = val / 1.0
                
            elif unit_str in ['lb']:
                converted = val * 0.45359237
                
            elif unit_str in ['oz']:
                converted = val * 0.0283495231
            
            else: # Default to grams if unknown string or missing value logic above didn't catch it properly as a number but treated as g
                 converted = val / 1.0

            return round(converted, 6)
            
        except Exception:
            return None
    
    result_list = []
    
    for item in measurements:
        try:
            # Attempt to parse the item. If it's already a number (int/float), treat as grams. 
            # Otherwise assume list/tuple format [value, unit].
            
            if isinstance(item, (list, tuple)):
                val = float(item[0])
                unit_str = str(item[1]).strip().lower() if len(item) > 1 else "g"
                
                conversion_map = {
                    'kg': lambda v: v / 1.0,
                    'lb': lambda v: v * 0.45359237,
                    'oz': lambda v: v * 0.0283495231,
                }
                
                converted = conversion_map.get(unit_str, lambda x: x / 1.0)(val)
            else:
                # Treat as a single number in grams
                val = float(item)
                unit_str = "g"
                converted = val
            
            result_list.append(converted)
            
        except (ValueError, TypeError):
            result_list.append(None)

    return result_list

if __name__ == '__main__':
    # Hard-coded sample values including various units and potential edge cases
    
    samples = [
        [[50.0, "kg"], 1234],           # Valid kg, valid g (default), invalid format -> None? No, let's make it robust: 
                                        # Actually the logic above handles single numbers as grams.
                                        # Let's adjust sample to be explicit tuples/lists for clarity in testing error handling if needed,
                                        # but per spec we want graceful handling.
        [[100, "g"], [2.5, "lb"]],     # Valid g and lb
        [["oz", 3]],                    # Invalid order (string first), handled by logic? No, my code expects value then unit.
                                        # Let's fix the sample to match expected input format for robustness or adjust function expectations.
                                        # Re-reading task: "takes a list of weight measurements". 
                                        # Common formats are [value, unit] or just value (g).
        [[10, "kg"], ["lb", 5], 2436], # Mixed valid types and defaults
    
    ]

    # Let's refine the input format for clarity in samples to ensure they represent real use cases.
    # Sample inputs: 
    # [value] -> grams
    # [value, unit_string] or (value, unit_string)
    
    refined_samples = [
        [[50, "kg"], 1234],            # 50 kg and 1234 g
        [[1.8, "lb"]],                  # 1.8 lb
        [[64, "oz"]],                   # 64 oz
        [["invalid", 10]],              # Invalid unit string -> treated as 'g' or error? My code treats unknown unit as /1 (grams) but logic above has a catch-all for g. 
                                        # Wait, if unit_str is not in map and not empty/g/oz/lb/kg, it defaults to val/1.0 which is grams.
                                        # So "invalid" becomes 64g? No, value was 10. Unit string "invalid". It goes to else -> converted = val / 1.0 (grams). Correct behavior for unknown units here: treat as g.
        [[25]],                         # Just a number -> grams
    ]

    print("Original Measurements:")
    for s in refined_samples:
        print(s)
    
    result_list = convert_to_kilograms(refined_samples)
    
    print("\nConverted to Kilograms (None represents invalid/unprocessable data):")
    for item, converted in zip(refined_samples, result_list):
        if item is not None and converted is not None: # Skip original 'invalid' check logic here since we want output list too. 
            val_str = str(item) if isinstance(item, (list,tuple)) else f"{item}"
            print(f"Input: {val_str} -> Output: {converted}")
        elif item is None or converted is None: # Show what happened with errors/invalids
             pass 
        
    # Explicitly showing the result list for clarity in this specific run block context without excessive printing of internals if not needed.
    print("\nFinal Result List:")
    for i, res in enumerate(result_list):
        status = "Valid" if res is not None else "Invalid/Unprocessable"
        print(f"[{i}] {res} ({status})")