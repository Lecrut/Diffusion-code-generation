def apply_capitalization_rule(s: str, rule: str) -> str:
    def title_case(text):
        return text.title()
    
    def upper_case(text):
        return text.upper()
    
    def lower_case(text):
        return text.lower()
    
    rules = {
        'title': title_case,
        'upper': upper_case,
        'lower': lower_case
    }
    
    if rule not in rules:
        raise ValueError("Unsupported capitalization rule")
    
    return rules[rule](s)

if __name__ == '__main__':
    sample_string = "this is a test"
    rule = 'upper'
    capitalized_string = apply_capitalization_rule(sample_string, rule)
    print(capitalized_string)