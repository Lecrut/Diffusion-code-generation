def run_length_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)
    
    return "".join(encoded)

def run_length_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        if encoded[i].isdigit():
            count_str = ""
            while i < len(encoded) and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            count = int(count_str)
            if i < len(encoded):
                decoded.append(encoded[i] * count)
                i += 1
        else:
            decoded.append(encoded[i])
            i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_data)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)