def apply_case_rule(text: str, rule: str, char: str) -> str:
    if rule == 'title':
        return text.capitalize()
    elif rule == 'upper':
        return text.upper()
    elif rule == 'lower':
        return text.lower()
    elif rule == 'title_char':
        if text:
            return text[0].upper() + text[1:]
        else:
            return ""
    else:
        return text
if __name__ == '__main__':
    sample_string = "hello world"
    sample_char = "W"
    result_title = apply_case_rule(sample_string, 'title', sample_char)
    result_upper = apply_case_rule(sample_string, 'upper', sample_char)
    result_lower = apply_case_rule(sample_string, 'lower', sample_char)
    result_title_char = apply_case_rule(sample_string, 'title_char', sample_char)
    result_default = apply_case_rule(sample_string, 'unknown', sample_char)
    print(f"Original String: {sample_string}")
    print(f"Rule 'title': {result_title}")
    print(f"Rule 'upper': {result_upper}")
    print(f"Rule 'lower': {result_lower}")
    print(f"Rule 'title_char': {result_title_char}")
    print(f"Rule 'unknown': {result_default}")