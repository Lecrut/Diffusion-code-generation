def get_first_letter(s):
    def is_valid_string(input_str):
        return isinstance(input_str, str)
    
    if not is_valid_string(s) or len(s) == 0:
        return ""
    
    return s[0]

if __name__ == '__main__':
    sample_values = ["Alibaba", "", "Cloud", "Qwen"]
    results = [get_first_letter(value) for value in sample_values]
    print(results)