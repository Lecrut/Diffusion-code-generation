import itertools
import json
import re

def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""

    compressed_parts = []
    groups = itertools.groupby(input_string)

    for char, group in groups:
        count = len(list(group))
        
        if count == 1:
            if char in ('(', ')', ','):
                compressed_parts.append(f"({char})")
            elif ord(char) > 127:
                compressed_parts.append(f"\\U{count:04d}{char}")
            else:
                compressed_parts.append(char)
        else:
            compressed_parts.append(f"({count},{char})")
            
    return "".join(compressed_parts)

def run_length_decode(compressed_string: str) -> str:
    if not compressed_string:
        return ""

    decoded_chars = []
    i = 0
    length = len(compressed_string)
    
    while i < length:
        char = compressed_string[i]
        
        if char == '\\':
            if i + 4 < length and compressed_string[i+1:i+3] == 'U{':
                count = int(compressed_string[i+3:i+4], 10)
                next_char = compressed_string[i+4]
                for _ in range(count):
                    decoded_chars.append(next_char)
                i += 5
                continue
            else:
                decoded_chars.append(char)
                i += 1
                continue
        elif char == '(':
            if i + 1 < length and compressed_string[i+1] == ')':
                decoded_chars.append(compressed_string[i+1])
                i += 3
                continue
            
            close_paren_index = compressed_string.find(')', i + 1)
            if close_paren_index == -1:
                break
                
            count_str = compressed_string[i+1:close_paren_index]
            try:
                count = int(count_str)
            except ValueError:
                decoded_chars.append(char)
                i += 1
                continue
                
            if i + close_paren_index + 2 < length:
                repeated_char = compressed_string[i + close_paren_index + 2]
                for _ in range(count):
                    decoded_chars.append(repeated_char)
                i = i + close_paren_index + 3
                continue
            else:
                break
        else:
            decoded_chars.append(char)
            i += 1

    return "".join(decoded_chars)

if __name__ == '__main__':
    test_input = "AAABBBCCCDaa"
    encoded = run_length_encode(test_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    
    unicode_input = "AaBbCc"
    unicode_encoded = run_length_encode(unicode_input)
    print(unicode_encoded)
    unicode_decoded = run_length_decode(unicode_encoded)
    print(unicode_decoded)