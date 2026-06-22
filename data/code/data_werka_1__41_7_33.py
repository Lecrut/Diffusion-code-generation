def format_string(s):
    def is_valid_string(input_str):
        return isinstance(input_str, str) and input_str.strip()
    
    if not is_valid_string(s):
        raise ValueError("Input must be a non-empty string")
    
    original = s
    all_caps = s.upper()
    sentence_case = s.capitalize()
    
    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_value = "hello world"
    formatted_result = format_string(sample_value)
    print(formatted_result)