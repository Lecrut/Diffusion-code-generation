def run_length_encode(data):
    if not data:
        return []
    
    iterator = iter(data)
    try:
        current_char = next(iterator)
    except StopIteration:
        return []
    
    count = 1
    result = []
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def decode_rle(encoded_data):
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)
    
    large_sample = "A" * 1000 + "B" * 500 + "C" * 250
    large_encoded = run_length_encode(large_sample)
    print(large_encoded)
    large_decoded = decode_rle(large_encoded)
    print(len(large_decoded))