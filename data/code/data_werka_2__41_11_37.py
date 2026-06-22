def capitalize_string(s: str, rule: str) -> str:
    RULE_TITLE = 'title'
    RULE_UPPER = 'upper'
    RULE_LOWER = 'lower'
    
    if rule == RULE_TITLE:
        return s.title()
    elif rule == RULE_UPPER:
        return s.upper()
    elif rule == RULE_LOWER:
        return s.lower()
    else:
        raise ValueError("Unsupported capitalization rule")

if __name__ == '__main__':
    sample_string = "hello world"
    rule = 'title'
    capitalized_string = capitalize_string(sample_string, rule)
    print(capitalized_string)