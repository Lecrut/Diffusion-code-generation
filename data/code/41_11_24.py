def capitalize_string(s, rule):
    if rule == 'title':
        return s.title()
    elif rule == 'upper':
        return s.upper()
    elif rule == 'lower':
        return s.lower()
    else:
        raise ValueError("Unsupported rule")

if __name__ == '__main__':
    sample_string = "hello world"
    rule = 'title'
    result = capitalize_string(sample_string, rule)
    print(result)