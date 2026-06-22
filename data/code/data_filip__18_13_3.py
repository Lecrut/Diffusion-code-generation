def run_length_encode(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def run_length_decode(encoded):
    if not encoded:
        return ""
    result = []
    for char, count in encoded:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample1 = "AAABBBCCCDAA"
    sample2 = "ABCDEF"
    sample3 = "AAAAAAAAAA"
    
    encoded1 = run_length_encode(sample1)
    decoded1 = run_length_decode(encoded1)
    
    encoded2 = run_length_encode(sample2)
    decoded2 = run_length_decode(encoded2)
    
    encoded3 = run_length_encode(sample3)
    decoded3 = run_length_decode(encoded3)
    
    print(encoded1)
    print(decoded1)
    print(encoded2)
    print(decoded2)
    print(encoded3)
    print(decoded3)