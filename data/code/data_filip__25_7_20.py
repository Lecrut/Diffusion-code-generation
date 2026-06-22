def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def check_compression_effectiveness(s):
    encoded = run_length_encode(s)
    original_len = len(s)
    encoded_len = len(encoded)
    is_effective = encoded_len < original_len
    return {
        "original_string": s,
        "encoded_string": encoded,
        "original_length": original_len,
        "encoded_length": encoded_len,
        "compression_effective": is_effective
    }

if __name__ == '__main__':
    sample_string = "AAAAAAAAAAABBBBBBBBCCCC"
    result = check_compression_effectiveness(sample_string)
    print(result["original_string"])
    print(result["encoded_string"])
    print(result["original_length"])
    print(result["encoded_length"])
    print(result["compression_effective"])