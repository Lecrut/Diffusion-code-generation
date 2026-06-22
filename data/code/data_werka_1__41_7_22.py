def format_string(input_str):
    all_caps = input_str.upper()
    sentence_case = input_str.capitalize()
    formatted_str = f"{input_str}, {all_caps}, {sentence_case}"
    return formatted_str

if __name__ == '__main__':
    sample_input = "hello world"
    result = format_string(sample_input)
    print(result)