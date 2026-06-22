def rle_encode(data, max_run_length):
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char and count < max_run_length:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    
    result.append((current_char, count))
    return result

def rle_decode(encoded_data):
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == "__main__":
    sample_input = "AAAAABBBBCCCCCDDDDDD"
    limit = 5
    encoded = rle_encode(sample_input, limit)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)