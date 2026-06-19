def capitalize_string(s: str, rule: str) -> str:
    rules = {
        'title': s.title,
        'upper': s.upper,
        'lower': s.lower,
        'swapcase': s.swapcase
    }
    if rule not in rules:
        raise ValueError("Unsupported capitalization rule")
    return rules[rule]()

if __name__ == '__main__':
    sample_string = "hello world"
    rule = 'title'
    capitalized_string = capitalize_string(sample_string, rule)
    print(capitalized_string)