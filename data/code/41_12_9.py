import sys

def validate_input_string(data: str) -> bool:
    """Validate that input data is a non-empty string."""
    if isinstance(data, str):
        return len(data.strip()) > 0
    else:
        raise TypeError("Input must be a string.")

def get_case_manipulation_rule(rule_str: str = "") -> dict[str, any]:
    """Parse the case manipulation rule into an executable function."""
    rules_map = {
        'swap': lambda s: ''.join(s[i].lower() if i % 2 == 0 else s[i].upper() for i in range(len(s))),
        'titlecase': str.title,
        'uppercase': str.upper,
        'lowercase': str.lower,
    }

    rule_upper = rule_str.strip().lower()
    
    # Default to swap if no valid rule is provided or input is invalid
    default_rule = rules_map.get('swap', lambda s: s) 

    return {
        'function': rules_map.get(rule_upper, default_rule),
        'is_valid': True
    }

def process_string(input_str: str, rule_func: callable) -> tuple[str, bool]:
    """Apply the case manipulation function to the input string."""
    try:
        result = rule_func(input_str.strip())
        
        # Ensure output is a string even if the function returns something else (unlikely for standard cases)
        return str(result), True
        
    except Exception as e:
        error_msg = f"Error applying transformation: {str(e)}"
        print(error_msg, file=sys.stderr)
        return "", False

def main():
    """Main entry point executing the logic with hard-coded sample values."""
    
    # Hard-coded sample input and rule to satisfy non-interactive requirement
    SAMPLE_INPUT = "Hello World This Is Python Script"
    RULE_SPECIFICATION = 'swap'  # User-specified case manipulation rule
    
    try:
        raw_input_data = str(SAMPLE_INPUT)

        # Step 1: Validate Input String
        validate_input_string(raw_input_data)

        # Step 2: Parse and Get the Case Manipulation Rule Function
        parsed_rule_info = get_case_manipulation_rule(RULE_SPECIFICATION)
        
        if not parsed_rule_info['is_valid']:
            raise ValueError("Invalid case manipulation rule provided.")

        transform_func = parsed_rule_info['function']

        # Step 3: Process the String
        final_output, execution_success = process_string(raw_input_data, transform_func)

    except TypeError as te:
        print(f"Input Validation Error: {te}", file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(f"Configuration Error: {ve}", file=sys.stderr)
        sys.exit(1)
    
    # Step 4: Output Result to Standard Output if successful
    if execution_success and final_output is not None:
        print(final_output)

if __name__ == '__main__':
    main()