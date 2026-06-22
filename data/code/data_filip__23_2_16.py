def run_length_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(data):
    if not data:
        return ""
    result = []
    i = 0
    n = len(data)
    while i < n:
        current_char = ""
        while i < n and data[i].isdigit():
            current_char += data[i]
            i += 1
        if i < n:
            count = int(current_char) if current_char else 0
            char = data[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDD"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")