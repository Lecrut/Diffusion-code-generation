def _validate_input(value):
    if not isinstance(value, str):
        raise TypeError("Expected a string")
    return value

def has_duplicate_chars(text):
    validated_text = _validate_input(text)
    return len(validated_text) != len(set(validated_text))

if __name__ == '__main__':
    sample_value = "banana"
    output = has_duplicate_chars(sample_value)
    print(output)