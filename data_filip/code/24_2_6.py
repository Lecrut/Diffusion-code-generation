def rle_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def rle_decode(encoded):
    result = []
    for char, count in encoded:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(decoded)