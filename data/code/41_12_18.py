import sys

def validate_input_string(s: str) -> bool:
    """Validate that the input string is non-empty."""
    return len(s.strip()) > 0

def apply_swap_case_rule(text: str) -> str:
    """Swap case for all alphabetic characters in the text.
    
    Args:
        text (str): The input string to manipulate.
        
    Returns:
        str: A new string with swapped cases.
    """
    result = []
    for char in text:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

def process_string(input_str: str, rule: str = 'swap') -> dict:
    """Process the input string based on the specified rule.
    
    Args:
        input_str (str): The raw input string.
        rule (str): The manipulation rule ('swap' is default).
        
    Returns:
        dict: A dictionary containing status, original_input, and result if successful;
              or an error message if validation fails.
    """
    # Validate the provided string content
    clean_str = input_str.strip()
    
    if not validate_input_string(clean_str):
        return {
            'status': 'error',
            'message': f'Input is invalid: Empty string after stripping whitespace.',
            'original_input': None,
            'result': None
        }

    # Apply the rule (currently only swap case implemented)
    try:
        processed_text = apply_swap_case_rule(clean_str)
        
        return {
            'status': 'success',
            'message': f'String successfully transformed using "{rule}" rule.',
            'original_input': clean_str,
            'result': processed_text
        }
    
    except Exception as e:
        return {
            'status': 'error',
            'message': f'An unexpected error occurred during processing: {str(e)}',
            'original_input': None,
            'result': None
        }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    
    # Sample 1: Basic string with mixed case and numbers
    SAMPLE_INPUT_1 = "Hello World! This is a test."
    RULE_1 = 'swap'

    # Sample 2: String containing only special characters (edge case for validation)
    SAMPLE_INPUT_2 = "!@#$%^&*()"
    
    # Sample 3: Empty string after stripping whitespace
    SAMPLE_INPUT_3 = "   "

    test_cases = [
        {
            'name': 'Mixed Case Text',
            'input_data': SAMPLE_INPUT_1,
            'rule_to_use': RULE_1
        },
        {
            'name': 'Special Characters Only',
            'input_data': SAMPLE_INPUT_2,
            'rule_to_use': RULE_1
        },
        {
            'name': 'Whitespace Only (Validation Test)',
            'input_data': SAMPLE_INPUT_3,
            'rule_to_use': RULE_1
        }
    ]

    for test_case in test_cases:
        print(f"\n--- Processing Sample: {test_case['name']} ---")
        
        # Simulate reading from standard input using the provided string directly.
        raw_input = test_case['input_data']
        
        result_dict = process_string(raw_input, rule=test_case['rule_to_use'])
        
        if result_dict['status'] == 'success':
            print(f"Original Input: '{result_dict['original_input']}'")
            print(f"Transformed Output: '{result_dict['result']}'")
        else:
            print(f"Error: {result_dict['message']}")