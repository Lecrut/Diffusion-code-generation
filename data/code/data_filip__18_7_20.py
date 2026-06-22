def run_length_encode(data):
    if not data:
        return ""
    result_parts = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result_parts.append(str(count))
            result_parts.append(current_char)
            current_char = char
            count = 1
    result_parts.append(str(count))
    result_parts.append(current_char)
    return "".join(result_parts)

if __name__ == '__main__':
    sample_string = "AAABBBCCCDDE"
    encoded = run_length_encode(sample_string)
    print(encoded)