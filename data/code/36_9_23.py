def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Qwen, Alibaba Cloud AI"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)