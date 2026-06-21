def enhanced_rle_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    escape_char = '\\'
    i = 1
    while i < len(data):
        next_char = data[i]
        if next_char == escape_char and i + 1 < len(data):
            following_char = data[i + 1]
            if following_char.isdigit():
                result.append(escape_char)
                result.append(str(count))
                count = 1
                current_char = following_char
                i += 2
                continue
            else:
                result.append(escape_char)
                result.append(str(count))
                count = 1
                current_char = escape_char
                result.append(escape_char)
                i += 2
                continue
        if next_char == current_char and not (next_char == escape_char and i + 1 < len(data) and data[i + 1].isdigit()):
            count += 1
            i += 1
        else:
            if count > 1:
                result.append(escape_char)
                result.append(str(count))
            result.append(current_char)
            current_char = next_char
            count = 1
            i += 1
    if count > 1:
        result.append(escape_char)
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

def enhanced_rle_decode(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        char = data[i]
        if char == '\\':
            if i + 1 < len(data) and data[i + 1].isdigit():
                count_str = ""
                j = i + 1
                while j < len(data) and data[j].isdigit():
                    count_str += data[j]
                    j += 1
                count = int(count_str)
                i = j
                if i < len(data):
                    next_char = data[i]
                    if next_char == '\\':
                        result.append('\\')
                    else:
                        result.append(next_char * count)
                    i += 1
                else:
                    break
            elif i + 1 < len(data):
                next_char = data[i + 1]
                result.append(next_char)
                i += 2
            else:
                result.append(char)
                i += 1
        else:
            result.append(char)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCDD22\\22"
    encoded = enhanced_rle_encode(sample_input)
    print(encoded)
    decoded = enhanced_rle_decode(encoded)
    print(decoded)