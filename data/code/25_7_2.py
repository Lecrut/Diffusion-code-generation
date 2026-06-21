def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

def compare_compression_effectiveness(s):
    if not s:
        return {"original_length": 0, "encoded_length": 0, "compressed": False}
    encoded_string = run_length_encode(s)
    original_length = len(s)
    encoded_length = len(encoded_string)
    return {
        "original_length": original_length,
        "encoded_length": encoded_length,
        "compressed": encoded_length < original_length
    }

if __name__ == '__main__':
    sample_string = "wwwwaaadexxxxxx"
    result = compare_compression_effectiveness(sample_string)
    print(result)