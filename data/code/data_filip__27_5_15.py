RLE_MARKER = '\x00'

def encode_rle(text):
    if not text:
        return ""
    padded = text + RLE_MARKER
    parts = []
    current_run_char = text[0]
    current_run_count = 0
    for char, next_char in zip(text, padded):
        if char == current_run_char:
            current_run_count += 1
        else:
            if current_run_count > 1:
                parts.append(str(current_run_count))
            parts.append(current_run_char)
            current_run_char = char
            current_run_count = 1
    return ''.join(parts)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    encoded_result = encode_rle(sample_input)
    print(encoded_result)