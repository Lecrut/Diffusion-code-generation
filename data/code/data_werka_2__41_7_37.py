def format_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    original = s
    all_caps = s.upper()
    sentence_case = s.capitalize()
    
    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_input = "hello world"
    result = format_string(sample_input)
    print(result)