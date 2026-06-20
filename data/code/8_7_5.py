def split_and_filter_csv(input_str):
    parts = input_str.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_input = "  apple , banana,,  ,cherry  , ,date "
    output = split_and_filter_csv(sample_input)
    print(output)