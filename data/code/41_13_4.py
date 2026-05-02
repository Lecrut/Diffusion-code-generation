def apply_case_rule(text: str, rule: str) -> str:
    if rule == 'title':
        return text.capitalize()
    elif rule == 'upper':
        return text.upper()
    elif rule == 'lower':
        return text.lower()
    elif rule == 'titlecase':
        return text.title()
    else:
        return text
if __name__ == '__main__':
    sample_string = "hello world"
    sample_char = 'w'
    result_title = apply_case_rule(sample_string, 'title')
    result_upper = apply_case_rule(sample_string, 'upper')
    result_lower = apply_case_rule(sample_string, 'lower')
    result_titlecase = apply_case_rule(sample_string, 'titlecase')
    result_default = apply_case_rule(sample_string, 'unknown')
    print(f"Original String: {sample_string}")
    print(f"Rule 'title': {result_title}")
    print(f"Rule 'upper': {result_upper}")
    print(f"Rule 'lower': {result_lower}")
    print(f"Rule 'titlecase': {result_titlecase}")
    print(f"Rule 'unknown': {result_default}")