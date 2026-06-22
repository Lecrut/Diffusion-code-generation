STRING_LENGTH_CONSTANT = 1

def calculate_string_length(s):
    return len(s) * STRING_LENGTH_CONSTANT

if __name__ == '__main__':
    sample_string = "Qwen, Alibaba Cloud's AI Assistant"
    print(calculate_string_length(sample_string))