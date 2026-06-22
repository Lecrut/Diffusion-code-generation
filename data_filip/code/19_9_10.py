def enhanced_rle_encode(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        current_char = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == current_char:
            count += 1
            if count == 255:
                break
        if current_char.isdigit() or current_char == '#':
            result.append('#')
            result.append(str(count))
            result.append(current_char)
        elif count > 1:
            result.append(str(count))
            result.append(current_char)
        else:
            if current_char == '#':
                result.append('#')
                result.append('1')
                result.append(current_char)
            else:
                result.append(current_char)
        i += count
    return "".join(result)

def enhanced_rle_decode(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        char = data[i]
        if char == '#':
            if i + 2 < len(data):
                count = int(data[i + 1])
                literal = data[i + 2]
                result.append(literal * count)
                i += 3
            else:
                result.append('#')
                i += 1
        elif char.isdigit():
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            if i < len(data):
                count = int(count_str)
                result.append(data[i] * count)
                i += 1
            else:
                result.append("#" + count_str)
        else:
            result.append(char)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBB#C#D###111"
    encoded = enhanced_rle_encode(sample_string)
    print(encoded)
    decoded = enhanced_rle_decode(encoded)
    print(decoded)