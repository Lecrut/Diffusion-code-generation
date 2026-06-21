def run_length_encode(text):
    if not text:
        return {}
    result = {}
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

def run_length_decode(encoded_dict):
    decoded = []
    for char, count in encoded_dict.items():
        decoded.append(char * count)
    return ''.join(decoded)
if __name__ == '__main__':
    sample_text = 'AAAABBBCCDAA'
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)
    sample_text_2 = 'z'
    encoded_2 = run_length_encode(sample_text_2)
    print(encoded_2)
    sample_text_3 = 'aabcccaaa'
    encoded_3 = run_length_encode(sample_text_3)
    print(encoded_3)