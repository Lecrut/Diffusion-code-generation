def run_length_encode(text):
    if not text:
        return {}
    
    result = {}
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = text[i]
            count = 1
    
    result[current_char] = count
    return result

def run_length_decode(encoded):
    result = []
    for char, count in encoded.items():
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCD"
    encoded = run_length_encode(sample_text)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    sample_text2 = "hello world"
    encoded2 = run_length_encode(sample_text2)
    print(encoded2)
    
    decoded2 = run_length_decode(encoded2)
    print(decoded2)