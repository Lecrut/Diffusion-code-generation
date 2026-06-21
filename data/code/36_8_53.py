def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def is_empty_or_single_char(string):
        return len(string) <= 1
    
    if is_empty_or_single_char(s):
        return s
    
    mid = len(s) // 2
    left_half = s[:mid]
    right_half = s[mid:]
    
    reversed_left = reverse_string(right_half)
    reversed_right = reverse_string(left_half)
    
    return reversed_left + reversed_right

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