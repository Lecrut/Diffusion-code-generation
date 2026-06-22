def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded):
    decoded_parts = [char * count for char, count in encoded]
    return ''.join(decoded_parts)

def encode_generator(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

def decode_generator(encoded):
    for char, count in encoded:
        yield char * count

def compress_string(s):
    return list(encode_generator(s))

def decompress_string(encoded):
    return ''.join(decode_generator(encoded))

if __name__ == '__main__':
    sample1 = "aaaabbbcc"
    encoded1 = compress_string(sample1)
    decoded1 = decompress_string(encoded1)
    print(f"Original: {sample1}")
    print(f"Encoded: {encoded1}")
    print(f"Decoded: {decoded1}")
    
    sample2 = "abc"
    encoded2 = compress_string(sample2)
    decoded2 = decompress_string(encoded2)
    print(f"Original: {sample2}")
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {decoded2}")
    
    sample3 = ""
    encoded3 = compress_string(sample3)
    decoded3 = decompress_string(encoded3)
    print(f"Original: '{sample3}'")
    print(f"Encoded: {encoded3}")
    print(f"Decoded: '{decoded3}'")