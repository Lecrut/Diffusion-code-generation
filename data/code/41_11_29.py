def validate_rule(rule):
    supported_rules = ['title', 'upper', 'lower']
    if rule not in supported_rules:
        raise ValueError(f"Unsupported capitalization rule: {rule}")

def capitalize_string(s, rule):
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