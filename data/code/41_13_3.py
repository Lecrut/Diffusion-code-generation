def capitalize_string(text: str, rule: str) -> str:
    if rule == 'title':
        return text.capitalize()
    elif rule == 'upper':
        return text.upper()
    elif rule == 'lower':
        return text.lower()
    else:
        return text
if __name__ == '__main__':
    sample_string = "hello world"
    sample_char = 'w'
    result_title = capitalize_string(sample_string, 'title')
    result_upper = capitalize_string(sample_string, 'upper')
    result_lower = capitalize_string(sample_string, 'lower')
    result_default = capitalize_string(sample_string, 'unknown')
    print(f"Original String: {sample_string}")
    print(f"Rule 'title': {result_title}")
    print(f"Rule 'upper': {result_upper}")
    print(f"Rule 'lower': {result_lower}")
    print(f"Rule 'unknown': {result_default}")