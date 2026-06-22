def split_and_strip(input_string):
    if not input_string:
        return []
    parts = input_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_data = "apple,  banana , ,  orange,  grape  ,kiwi, ,lemon"
    output_list = split_and_strip(sample_data)
    print(output_list)