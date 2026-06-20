def split_string_by_commas(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    parts = text.split(',')
    trimmed_parts = [part.strip() for part in parts]
    result = [part for part in trimmed_parts if part]
    return result

if __name__ == '__main__':
    sample_input = "  apple ,  banana  ,  orange ,  , grape  "
    output = split_string_by_commas(sample_input)
    print(output)