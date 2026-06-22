def split_and_trim(s):
    if not s:
        return []
    parts = s.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_string = "  apple, banana , , orange,  , grape  "
    output_list = split_and_trim(sample_string)
    print(output_list)