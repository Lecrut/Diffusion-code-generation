def compress_string(input_string):
    if not input_string:
        return ""
    result = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def decompress_string(encoded_string):
    result = []
    chars = list(encoded_string)
    i = 0
    while i < len(chars):
        char = chars[i]
        i += 1
        num_str = ""
        while i < len(chars) and chars[i].isdigit():
            num_str += chars[i]
            i += 1
        count = int(num_str) if num_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAAAAAAABBBBBBBBCCCCCDDDDDDDDDD"
    compressed = compress_string(sample_input)
    print(compressed)
    decompressed = decompress_string(compressed)
    print(decompressed)