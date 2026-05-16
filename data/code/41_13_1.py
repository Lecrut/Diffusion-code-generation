def capitalize_string(text: str, rule: str) -> str:
    if rule == 'title':
        return text.capitalize()
    elif rule == 'upper':
        return text.upper()
    elif rule == 'lower':
        return text.lower()
    elif rule == 'sentence':
        return text.capitalize()
    else:
        return text
if __name__ == '__main__':
    input_string = "hello world"
    char_to_capitalize = 'w'
    print(f"Original String: {input_string}")
    result_title = capitalize_string(input_string, 'title')
    print(f"Title Case: {result_title}")
    result_upper = capitalize_string(input_string, 'upper')
    print(f"Upper Case: {result_upper}")
    result_lower = capitalize_string(input_string, 'lower')
    print(f"Lower Case: {result_lower}")
    result_sentence = capitalize_string(input_string, 'sentence')
    print(f"Sentence Case: {result_sentence}")
    result_default = capitalize_string(input_string, 'unknown')
    print(f"Default Case: {result_default}")