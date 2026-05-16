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
    result_title = capitalize_string(sample_string, 'title')
    result_upper = capitalize_string(sample_string, 'upper')
    result_lower = capitalize_string(sample_string, 'lower')
    result_default = capitalize_string(sample_string, 'unknown')
    print(f"Original: {sample_string}")
    print(f"Title: {result_title}")
    print(f"Upper: {result_upper}")
    print(f"Lower: {result_lower}")
    print(f"Default: {result_default}")