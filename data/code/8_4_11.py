def process_comma_separated_string(input_text):
    raw_parts = input_text.split(',')
    cleaned_parts = []
    for part in raw_parts:
        stripped_value = part.strip()
        cleaned_parts.append(stripped_value)
    return cleaned_parts

if __name__ == '__main__':
    test_data = "  dog , cat , elephant , giraffe  "
    output_list = process_comma_separated_string(test_data)
    print(output_list)