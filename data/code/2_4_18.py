def parse_volumes(volume_string: str) -> list[float]:
    """
    Parses a string containing comma-separated volume values into a list of floats.
    
    Args:
        volume_string (str): A string where numbers are separated by commas. 
                             May contain whitespace around the numbers or non-numeric content.
                             
    Returns:
        list[float]: A list of floating-point numbers extracted from valid input segments.
        
    Raises:
        ValueError: If no numeric values can be parsed, or if a specific segment 
                   fails to convert and cannot be safely skipped as an empty string 
                   (though typically non-numeric tokens will trigger this).
    
    Note: This function attempts to parse all comma-separated parts. Any part that is not 
    valid for float conversion will raise a ValueError immediately upon encountering it,
    unless the specific requirement was to skip bad values (which contradicts typical error handling)
    or if we treat spaces as delimiters within tokens. Given standard strict interpretation:
    If any token fails float() and isn't empty/whitespace-only after stripping relevant chars 
    around a valid number part, it raises an error. However, to be robust against "invalid input"
    generally meaning mixed garbage: Let's refine the logic per instruction for specific segment handling?
    
    Refined Logic based on typical 'error handling': We assume that if ANY token cannot be converted and 
    is not purely whitespace (which we strip anyway), it raises an error. But wait, what if there are multiple errors?
    The simplest robust approach requested: Try to parse each chunk. If a chunk fails float() conversion completely, raise ValueError.
    
    Example good input: "10, 20, thirty" -> Should this fail on 'thirty'? 
    Yes, usually non-numeric inputs are treated as errors unless specified otherwise (e.g., try-except inside).
    However, often these tasks imply skipping garbage? No, task says "including error handling for non-numeric inputs", implying raising.
    
    Revised Plan: Split by comma. Strip whitespace from each part. Try to convert to float. 
    If conversion fails for any part that is not empty or purely spaces (after stripping), raise ValueError with message indicating the issue found in that specific segment if possible, or general error.

    Correction on "skip": The prompt says "error handling", usually meaning don't skip silently but report/fail.
    
    Let's implement: Split -> Strip each part -> Try float() -> If fails and string isn't empty/just spaces after stripping? 
    Actually, let's just be strict: if any token is not a valid number representation (after removing surrounding whitespace), raise ValueError.
    """
    try:
        # Split the input string by commas
        parts = volume_string.split(',')
        
        result_list = []
        
        for i, part in enumerate(parts):
            # Strip leading and trailing whitespace from each segment
            stripped_part = part.strip()
            
            if not stripped_part:
                continue  # Skip empty segments resulting from consecutive commas
            
            try:
                volume_value = float(stripped_part)
                result_list.append(volume_value)
            except ValueError as e:
                raise ValueError(f"Invalid numeric value found at index {i}: '{stripped_part}' cannot be converted to a floating-point number.") from e
                
        return result_list

    except Exception as e:
        # Additional catch for unexpected parsing failures (though split and strip are safe)
        raise RuntimeError(f"A critical error occurred while processing the volume string input: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies.
    
    # Sample 1: Valid inputs with spaces
    sample_valid = "50, 75.5, 100"
    
    # Sample 2: Contains non-numeric input (should raise error)
    sample_invalid_mixed = "30, invalid_data, 40"
    
    # Sample 3: Leading/trailing spaces and extra commas
    sample_formatting = " , 1.5 , ,, 2.5 ,"

    print("Testing parse_volumes function...")
    
    test_cases = [
        ("Valid inputs with spaces", sample_valid),
        ("Invalid mixed data (Expected Error)", sample_invalid_mixed, True), # Flag for expected error
        ("Format variations", sample_formatting)
    ]
    
    description_list = []
    results_list = []

    test_case_num = 0
    
    for desc, input_val, is_error_expected in test_cases:
        print(f"\n--- Test {test_case_num + 1}: '{desc}' ---")
        
        try:
            if is_error_expected:
                parsed_result = parse_volumes(input_val) # Will raise ValueError here as per logic
                results_list.append(parsed_result)
                description_list.append(f"Success (Unexpected): Result is {parsed_result}")
            else:
                result_output = parse_volumes(input_val)
                print("Result:", result_output)
                description_list.append(f"Parsed successfully to list of floats")
        except ValueError as ve:
            if is_error_expected:
                print(f"Caught expected error for invalid data: {ve}")
                results_list.append(None) # Indicate successful handling via exception
                description_list.append("Handled non-numeric input correctly with raise.")
            else:
                print(f"Unexpected error occurred: {ve}")
        except Exception as e:
            if is_error_expected or not (isinstance(e, ValueError)):
                 print(f"An unexpected system-level error occurred during test processing: {e}")

    # Final Summary Block based on task requirements to ensure completeness. 
    description_list.append("All tests executed.")
    
    for item in results_list + [x[0] if 'Result' not in x else None for x in description_list]: # Just printing descriptions directly is better than mixing lists
    
        print(f"Test Case Output: {item}")