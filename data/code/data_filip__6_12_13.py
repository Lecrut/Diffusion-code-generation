def _validate_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return True

def replace_spaces_with_underscores(text):
    _validate_text(text)
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_input = "the quick brown fox"
    transformed_output = replace_spaces_with_underscores(sample_input)
    print(transformed_output)