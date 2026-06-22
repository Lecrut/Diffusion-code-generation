def rle_encode(text):
    if not text:
        return ''
    encoded = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = text[i]
            count = 1
    encoded.append(str(count) + current_char)
    return ''.join(encoded)

def rle_decode(encoded):
    if not encoded:
        return ''
    decoded = []
    i = 0
    while i < len(encoded):
        count_str = ''
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        if i < len(encoded):
            char = encoded[i]
            decoded.append(char * count)
            i += 1
    return ''.join(decoded)

if __name__ == '__main__':
    sample_text = 'AAABBBCCCCDDEEEE'
    encoded = rle_encode(sample_text)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)