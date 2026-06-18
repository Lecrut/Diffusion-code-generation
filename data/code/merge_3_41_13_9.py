def capitalize_by_rule(text: str, char_to_match: str, rule: str) -> str:
    """
    Capitalizes characters in a string based on the specified rule.
    
    Supported rules: 'title' (capitalize first letter), 'upper_all', 'lower_first'.
    
    Args:
        text (str): The input string to process.
        char_to_match (str): A single character used for matching logic if applicable, 
                            currently acts as a placeholder for future rule extensions 
                            or specific match criteria in complex rules.
        rule (str): The capitalization rule ('title', 'upper_all', 'lower_first').
    
    Returns:
        str: New string with characters capitalized according to the rule.
    """
    if not text:
        return ""

    # Normalize inputs
    char_to_match = char_to_match[0] if isinstance(char_to_match, str) else ''
    rule_lower = rule.lower()

    result_list = []
    
    for i, c in enumerate(text):
        is_first_char = (i == 0 and text[i].isalpha()) or not text[i-1].isalnum() if i > 0 else True
        
        # Apply specific rules
        if rule_lower == 'title':
            result_list.append(c.upper() if is_first_char else c.lower())
        elif rule_lower == 'upper_all':
            result_list.append(c.upper())
        elif rule_lower == 'lower_first':
            result_list.append(char_to_match.upper() if char_to_match and i > 0 else c) # Placeholder logic for extension
        else:
            raise ValueError(f"Unsupported capitalization rule: {rule}")

    return "".join(result_list)

if __name__ == '__main__':
    sample_text = "hello world this is a test string"
    target_char = 'h'  # Example character to match or use as reference
    
    print("Original:", sample_text)
    
    rule1_result = capitalize_by_rule(sample_text, target_char, 'title')
    print(f"With 'title' rule: {rule1_result}")
    
    rule2_result = capitalize_by_rule(sample_text, target_char, 'upper_all')
    print(f"With 'upper_all' rule: {rule2_result}")