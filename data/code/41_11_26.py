def capitalize_string(s: str, rule: str) -> str:
    rules = {
        'title': s.title,
        'upper': s.upper,
        'lower': s.lower,
        'swapcase': s.swapcase
    }
    
    if rule in rules:
        return rules[rule]()
    else:
        raise ValueError("Unsupported capitalization rule")

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd ThIs Is A TeSt"
    rule = 'title'
    capitalized_string = capitalize_string(sample_string, rule)
    print(capitalized_string)