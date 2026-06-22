def run_length_encode(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    return "".join(compressed)

if __name__ == '__main__':
    sample_inputs = [
        "AABBBCCCC",
        "XYZ",
        "AAABBBCCC",
        "A",
        "AAAAAAAAAA",
        "",
        "ABABABAB"
    ]
    for sample in sample_inputs:
        result = run_length_encode(sample)
        print(f"Input: {sample!r} -> Output: {result!r}")