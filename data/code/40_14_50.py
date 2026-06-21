def is_valid_string(s):
    return isinstance(s, str) and len(s) > 0

def get_first_letter(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a non-empty string")
    return s[0]

if __name__ == '__main__':
    sample_string = "Qwen, Alibaba Cloud's AI Assistant"
    first_letter = get_first_letter(sample_string)
    print(first_letter)