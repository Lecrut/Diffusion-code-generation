def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def check_compression_efficiency(original_string):
    encoded_string = run_length_encode(original_string)
    original_length = len(original_string)
    encoded_length = len(encoded_string)
    is_efficient = encoded_length < original_length
    return {
        "original": original_string,
        "encoded": encoded_string,
        "original_length": original_length,
        "encoded_length": encoded_length,
        "is_efficient": is_efficient
    }

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    result = check_compression_efficiency(sample_text)
    print(result)