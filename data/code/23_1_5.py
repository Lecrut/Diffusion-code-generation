def run_length_encode(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
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
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            count = int(count_str) if count_str else 1
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    large_input = "A" * 10000 + "B" * 5000 + "C" * 2500
    encoded_large = run_length_encode(large_input)
    print(encoded_large)
    decoded_large = run_length_decode(encoded_large)
    print(decoded_large == large_input)