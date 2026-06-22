def format_string(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")
    
    original = input_str
    all_caps = input_str.upper()
    sentence_case = input_str.capitalize()
    
    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_input = "hello world"
    try:
        result = format_string(sample_input)
        print(result)
    except ValueError as e:
        print(e)