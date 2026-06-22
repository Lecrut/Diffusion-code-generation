def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_strings = ["", "a", "aa", "aabcccc", "AaAa", "112233"]
    for s in sample_strings:
        result = run_length_encode(s)
        print(f"Input: '{s}' -> Output: {result}")