import re

def run_length_encode_alphanumeric(s):
    filtered_chars = []
    for char in s:
        if char.isalnum():
            filtered_chars.append(char)
    
    if not filtered_chars:
        return {}
    
    result = {}
    current_char = filtered_chars[0]
    count = 1
    
    for i in range(1, len(filtered_chars)):
        if filtered_chars[i] == current_char:
            count += 1
        else:
            if current_char in result:
                result[current_char] += count
            else:
                result[current_char] = count
            current_char = filtered_chars[i]
            count = 1
    
    if current_char in result:
        result[current_char] += count
    else:
        result[current_char] = count
    
    return result

if __name__ == '__main__':
    sample_string = "aaabbCCCdd444"
    encoded_result = run_length_encode_alphanumeric(sample_string)
    print(encoded_result)