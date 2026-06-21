def enhanced_rle_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        current_char = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == current_char:
            count += 1
        if count > 1:
            result.append(f"{current_char}{count}")
        else:
            result.append(current_char)
        i += count
    return "".join(result)

def enhanced_rle_decode(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        char = data[i]
        if char.isdigit():
            raise ValueError("Invalid RLE format: unexpected digit at start")
        if i + 1 < len(data) and data[i + 1].isdigit():
            count_str = ""
            j = i + 1
            while j < len(data) and data[j].isdigit():
                count_str += data[j]
                j += 1
            count = int(count_str)
            result.append(char * count)
            i = j
        else:
            result.append(char)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBCDDDD!111"
    encoded = enhanced_rle_encode(sample_input)
    print(encoded)
    decoded = enhanced_rle_decode(encoded)
    print(decoded)
    special_input = "!!!111!!!"
    encoded_special = enhanced_rle_encode(special_input)
    print(encoded_special)
    decoded_special = enhanced_rle_decode(encoded_special)
    print(decoded_special)