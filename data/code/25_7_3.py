import re

def run_length_encode(s):
    if not s:
        return ''
    
    encoded = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return ''.join(encoded)

def is_compression_effective(s):
    encoded = run_length_encode(s)
    original_length = len(s)
    encoded_length = len(encoded)
    
    return encoded_length < original_length

if __name__ == '__main__':
    sample_strings = [
        "aaaabbbcc",
        "abcdef",
        "aaabbaaa",
        "aabbbcccc",
        "xyzz",
        "aaaaa",
        "ababab"
    ]
    
    for s in sample_strings:
        result = is_compression_effective(s)
        encoded = run_length_encode(s)
        original_len = len(s)
        encoded_len = len(encoded)
        print(f"Original: '{s}' (len={original_len}) -> Encoded: '{encoded}' (len={encoded_len}) -> Effective: {result}")