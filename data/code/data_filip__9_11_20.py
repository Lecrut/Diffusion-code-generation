def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    stripped = text.lstrip()
    result = stripped.rstrip()
    
    if result == "":
        return result
    
    start_idx = 0
    end_idx = len(result)
    
    while start_idx < end_idx and result[start_idx] == ' ':
        start_idx += 1
    
    while end_idx > start_idx and result[end_idx - 1] == ' ':
        end_idx -= 1
    
    return result[start_idx:end_idx]

if __name__ == '__main__':
    sample_input_1 = "  hello world  "
    sample_input_2 = "\t\n  spaced  \n\t"
    sample_input_3 = "nochange"
    sample_input_4 = ""
    sample_input_5 = "   leading spaces"
    sample_input_6 = "trailing spaces   "
    
    print(trim_string(sample_input_1))
    print(trim_string(sample_input_2))
    print(trim_string(sample_input_3))
    print(trim_string(sample_input_4))
    print(trim_string(sample_input_5))
    print(trim_string(sample_input_6))