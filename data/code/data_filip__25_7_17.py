def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

def is_compression_effective(original_string):
    encoded_string = run_length_encode(original_string)
    original_length = len(original_string)
    encoded_length = len(encoded_string)
    return original_length > encoded_length

if __name__ == '__main__':
    sample_string = "aaabbbcccaaa"
    result = is_compression_effective(sample_string)
    print(result)