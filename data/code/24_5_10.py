def run_length_encode(text):
    if not text:
        return []
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

def run_length_decode(encoded_data):
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    original = "aaabbc"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)