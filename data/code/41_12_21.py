import sys

def validate_input_case(rule: str) -> bool:
    """
    Validates that the provided case manipulation rule is supported.
    
    Args:
        rule (str): The user-specified rule string, e.g., 'swap', 'lower'.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    allowed_rules = {'upper', 'lower', 'capitalize', 'title', 'swap'}
    return rule.lower() in {rule for rule in allowed_rules}

def apply_case_rule(text: str) -> str:
    """
    Applies the specified case manipulation rule to the input text.
    
    Args:
        text (str): The string to manipulate.
        
    Returns:
        str: The manipulated string, or original if invalid rule provided internally.
    """
    # Handle specific known transformations manually for robustness and performance
    
    try:
        lower_rule = 'lower'
        upper_rule = 'upper'
        cap_rule = 'capitalize'
        title_rule = 'title'
        
        rule_map = {
            'swap': text.swapcase(), 
            'lower': text.lower(), 
            'upper': text.upper() if isinstance(text, str) else ''.join(char.upper() for char in text), # Fallback safety
            'capitalize': text.capitalize(), 
            'title': text.title()
        }
        
    except AttributeError:
        return text

    try:
        final_string = rule_map.get(rule.lower()) or text
        if not isinstance(final_string, str):
            final_string = ''.join(str(char).lower() for char in text) if rule == 'swap' else str(text)
    except Exception as e:
        print(f"Internal error during transformation {rule}: {e}", file=sys.stderr)
        
    return final_string

def main():
    """
    Main execution block.
    
    Simulates reading a string and applying case rules without using interactive prompts, sys.stdin input(), or argparse.
    The logic is embedded directly in the function scope to avoid external dependencies for argument parsing.
    """
    # Simulate standard input reading from a pre-defined sample value as per requirements
    
    if __name__ == '__main__':
        original_text = "Hello World! This Is A Test String."

    rule_to_apply = 'swap'
    
    try:
        result_string = apply_case_rule(original_text)
        print(result_string, end='\n')
        
    except Exception as e:
        print(f"Fatal error occurred during execution: {e}", file=sys.stderr)