def string_length(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return len(s)

if __name__ == '__main__':
    sample_string = "Qwen, created by Alibaba Cloud"
    print(string_length(sample_string))