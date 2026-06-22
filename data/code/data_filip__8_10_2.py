def split_and_trim(string_input):
    if not string_input:
        return []
    parts = string_input.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_data = "  apple , banana  ,  orange  , , grape "
    output_list = split_and_trim(sample_data)
    print(output_list)