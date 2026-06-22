def enhanced_rle_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        if count > 1:
            result.append(f"{count}{data[i]}")
        else:
            result.append(f"0{data[i]}")
        i += 1
    return "".join(result)

def enhanced_rle_decode(data: str) -> str:
    result = []
    i = 0
    while i < len(data):
        if i + 1 >= len(data):
            result.append(data[i])
            i += 1
            continue
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if not count_str:
            if i < len(data):
                result.append(data[i])
                i += 1
            continue
        count = int(count_str)
        if count == 0:
            if i < len(data):
                result.append(data[i])
                i += 1
        else:
            if i < len(data):
                result.append(data[i] * count)
                i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBBCC123!!"
    encoded = enhanced_rle_encode(sample_input)
    decoded = enhanced_rle_decode(encoded)
    print(encoded)
    print(decoded)