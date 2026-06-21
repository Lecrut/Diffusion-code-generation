def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + input_string[i - 1])
            count = 1
    encoded.append(str(count) + input_string[-1])
    return "".join(encoded)

def check_compression_effectiveness(original_string):
    encoded_string = run_length_encode(original_string)
    original_length = len(original_string)
    encoded_length = len(encoded_string)
    is_effective = encoded_length < original_length
    return {
        "original": original_string,
        "encoded": encoded_string,
        "original_length": original_length,
        "encoded_length": encoded_length,
        "compression_effective": is_effective
    }

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAABBB"
    result = check_compression_effectiveness(sample_input)
    print(f"Original: {result['original']} (Length: {result['original_length']})")
    print(f"Encoded: {result['encoded']} (Length: {result['encoded_length']})")
    print(f"Compression Effective: {result['compression_effective']}")