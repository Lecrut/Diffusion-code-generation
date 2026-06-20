def split_commas(s):
    if not s:
        return []
    parts = s.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_input = "apple, banana , ,orange, ,grape, "
    output = split_commas(sample_input)
    print(output)
    empty_input = ""
    output_empty = split_commas(empty_input)
    print(output_empty)
    complex_input = "  x ,  y ,z , ,  a b c  "
    output_complex = split_commas(complex_input)
    print(output_complex)