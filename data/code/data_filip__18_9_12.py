import sys

def run_length_encode(data: str) -> list:
    if not data:
        return []
    
    encoded = []
    count = 1
    current_char = data[0]
    length = len(data)
    
    i = 1
    while i < length:
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
        i += 1
    encoded.append((current_char, count))
    
    return encoded

def run_length_decode(encoded: list) -> str:
    decoded = []
    length = len(encoded)
    
    i = 0
    while i < length:
        char, count = encoded[i]
        decoded.append(char * count)
        i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCAAA"
    
    encoded = run_length_encode(sample_input)
    
    decoded = run_length_decode(encoded)
    
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {sample_input == decoded}")