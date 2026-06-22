def capitalize_string(s, rule):
    rules = {
        'title': str.title,
        'upper': str.upper,
        'lower': str.lower
    }
    
    if rule not in rules:
        raise ValueError("Unsupported capitalization rule")
    
    return rules[rule](s)

if __name__ == '__main__':
    sample_string = "hello world"
    rule = 'title'
    capitalized_string = capitalize_string(sample_string, rule)
    print(capitalized_string)