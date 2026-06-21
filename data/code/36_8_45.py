def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def is_valid_input(input_str):
        return isinstance(input_str, str)
    
    if not is_valid_input(s):
        raise ValueError("Input must be a string")
    
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string1 = "Hello, World!"
    reversed_string1 = reverse_string(sample_string1)
    print(reversed_string1)
    
    sample_string2 = "Alibaba Cloud"
    reversed_string2 = reverse_string(sample_string2)
    print(reversed_string2)
    
    sample_string3 = "Qwen, the AI assistant"
    try:
        reversed_string3 = reverse_string(sample_string3)
        print(reversed_string3)
    except ValueError as e:
        print(e)