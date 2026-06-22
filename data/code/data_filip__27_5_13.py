def run_length_encode(text):
    if not text:
        return ''
    encoded_parts = []
    char_count = 1
    padded = text + '\0'
    for current_char, next_char in zip(text, padded):
        if current_char == next_char:
            char_count += 1
        else:
            encoded_parts.append(current_char)
            if char_count > 1:
                encoded_parts.append(str(char_count))
            char_count = 1
    return ''.join(encoded_parts)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)