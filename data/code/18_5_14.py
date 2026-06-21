def run_length_encode(data: str) -> list:
    if not data:
        return []
    compressed = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = data[i]
            count = 1
    compressed.append((current_char, count))
    return compressed

def run_length_decode(encoded_data: list) -> str:
    decoded = []
    for char, count in encoded_data:
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_empty = ""
    sample_single = "z"
    sample_normal = "aaabbbcccc"
    
    encoded_empty = run_length_encode(sample_empty)
    encoded_single = run_length_encode(sample_single)
    encoded_normal = run_length_encode(sample_normal)
    
    print(encoded_empty)
    print(encoded_single)
    print(encoded_normal)
    
    decoded_empty = run_length_decode(encoded_empty)
    decoded_single = run_length_decode(encoded_single)
    decoded_normal = run_length_decode(encoded_normal)
    
    print(decoded_empty)
    print(decoded_single)
    print(decoded_normal)