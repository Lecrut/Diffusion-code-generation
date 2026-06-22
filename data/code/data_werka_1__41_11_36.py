def capitalize_string(s: str, rule: str) -> str:
    if rule == 'title':
        return s.title()
    elif rule == 'upper':
        return s.upper()
    elif rule == 'lower':
        return s.lower()
    else:
        raise ValueError("Unsupported capitalization rule")

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd ThIs Is A TeSt"
    rule = 'title'
    capitalized_string = capitalize_string(sample_string, rule)
    print(capitalized_string)