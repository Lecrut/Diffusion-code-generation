LENGTH_CONSTANT = 1

def string_length(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return len(s) * LENGTH_CONSTANT

if __name__ == '__main__':
    sample_string = "Qwen, Alibaba Cloud's AI Assistant"
    print(string_length(sample_string))