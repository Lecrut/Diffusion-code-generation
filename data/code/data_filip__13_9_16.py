def to_camel_case(text):
    if not text:
        return text
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_input = "convert_this_snake_case_string"
    result = to_camel_case(sample_input)
    print(result)