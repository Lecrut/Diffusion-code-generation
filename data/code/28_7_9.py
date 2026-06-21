def run_length_encode(s):
    if not s:
        return ""

    def _encode_generator():
        count = 1
        current_char = s[0]
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                yield str(count) + current_char
                current_char = char
                count = 1
        yield str(count) + current_char

    return ''.join(_encode_generator())

if __name__ == '__main__':
    sample_string = "AAABBBCCCDAA"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)