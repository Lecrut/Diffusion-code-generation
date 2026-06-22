def run_length_encode(data: str) -> str:
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
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
            
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

def run_length_decode(data: str) -> str:
    decoded = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            count = int(num_str)
            if i < len(data):
                decoded.append(data[i] * count)
                i += 1
        else:
            decoded.append(data[i])
            i += 1
            
    return "".join(decoded)

if __name__ == "__main__":
    sample_inputs = [
        "aabcccccaaa",
        "abcdef",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWWWWWWWWWWW",
        "",
        "A",
        "AABBCCDD",
        "1112233"
    ]
    
    for inp in sample_inputs:
        encoded = run_length_encode(inp)
        decoded = run_length_decode(encoded)
        print(f"Input: {inp!r}")
        print(f"Encoded: {encoded!r}")
        print(f"Decoded: {decoded!r}")
        print(f"Match: {inp == decoded}")
        print()