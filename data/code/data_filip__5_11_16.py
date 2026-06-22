def transform_strings(input_tuple):
    result = []
    for s in input_tuple:
        if len(s) == 0:
            result.append(s)
            continue
        first_char = s[0].upper()
        rest_chars = s[1:].lower()
        result.append(first_char + rest_chars)
    return tuple(result)

if __name__ == '__main__':
    sample_data = ("hELLO", "woRLD", "pyThOn", "tEsT")
    output_data = transform_strings(sample_data)
    print(output_data)