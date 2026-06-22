import sys

def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
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

def run_length_decode(data: str) -> str:
    if not data:
        return ""
    
    decoded = []
    length = len(data)
    i = 0
    
    while i < length:
        char = data[i]
        if char.isdigit():
            count_str = ""
            while i < length and data[i].isdigit():
                count_str += data[i]
                i += 1
            count = int(count_str)
            if i < length:
                run_char = data[i]
                decoded.append(run_char * count)
                i += 1
            else:
                decoded.append(count_str)
        else:
            decoded.append(char)
            i += 1
            
    return "".join(decoded)

if __name__ == '__main__':
    original_text = "aaabbbcccd"
    encoded = run_length_encode(original_text)
    print(f"Encoded: {encoded}")
    
    decoded_text = run_length_decode(encoded)
    print(f"Decoded: {decoded_text}")
    
    assert original_text == decoded_text
    
    empty = ""
    empty_encoded = run_length_encode(empty)
    print(f"Empty Encoded: {repr(empty_encoded)}")
    
    complex_text = "a" * 10 + "b" * 5 + "c"
    complex_encoded = run_length_encode(complex_text)
    print(f"Complex Encoded: {complex_encoded}")
    
    complex_decoded = run_length_decode(complex_encoded)
    print(f"Complex Decoded: {complex_decoded}")
    
    assert complex_text == complex_decoded
    
    single_char = "z"
    single_encoded = run_length_encode(single_char)
    print(f"Single Encoded: {single_encoded}")
    
    single_decoded = run_length_decode(single_encoded)
    print(f"Single Decoded: {single_decoded}")
    
    assert single_char == single_decoded