def validate_string_input(value):
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    return value

def capitalize_first_letter(text):
    validate_string_input(text)
    if len(text) == 0:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    examples = ["apple", "banana split", "123start", "", "z"]
    for item in examples:
        print(capitalize_first_letter(item))