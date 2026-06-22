def capitalize_string(s: str, rule: str) -> str:
    def validate_rule(rule: str):
        valid_rules = {'title', 'upper', 'lower'}
        if rule not in valid_rules:
            raise ValueError(f"Unsupported capitalization rule: {rule}")

    validate_rule(rule)
    
    if rule == 'title':
        return s.title()
    elif rule == 'upper':
        return s.upper()
    elif rule == 'lower':
        return s.lower()

if __name__ == '__main__':
    sample_string = "hello world"
    rule = 'title'
    capitalized_string = capitalize_string(sample_string, rule)
    print(capitalized_string)