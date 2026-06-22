def rle_encode(text):
    if not text:
        return []
    result = []
    count = 1
    for i in range(1, len(text) + 1):
        if i < len(text) and text[i] == text[i - 1]:
            count += 1
        else:
            result.append((text[i - 1], count))
            count = 1
    return result

def rle_decode(encoded):
    return ''.join(char * count for char, count in encoded)

def process_sample(text):
    encoded = rle_encode(text)
    decoded = rle_decode(encoded)
    return (encoded, decoded)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    encoded, decoded = process_sample(sample_text)
    print(encoded)
    print(decoded)