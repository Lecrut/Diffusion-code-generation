def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    n = len(data)
    i = 0
    while i < n:
        current_char = data[i]
        count = 1
        while i + 1 < n and data[i + 1] == current_char:
            i += 1
            count += 1
        if count > 9:
            result.append(str(count % 10))
            result.append(current_char)
            remaining = count // 10
            while remaining > 0:
                result.append(str(remaining % 10))
                result.append(current_char)
                remaining //= 10
        else:
            result.append(str(count))
            result.append(current_char)
        i += 1
    return "".join(result)

def run_length_decode(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    result = []
    n = len(encoded_data)
    i = 0
    while i < n:
        if not encoded_data[i].isdigit():
            result.append(encoded_data[i])
            i += 1
            continue
        count = 0
        while i < n and encoded_data[i].isdigit():
            count = count * 10 + int(encoded_data[i])
            i += 1
        if i < n:
            result.append(encoded_data[i] * count)
            i += 1
        else:
            break
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    assert sample_input == decoded