def split_and_clean(comma_separated_string):
    result = []
    parts = comma_separated_string.split(',')
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_input = "  apple , banana,, cherry , ,date "
    output = split_and_clean(sample_input)
    print(output)