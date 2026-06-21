def run_length_encode(text):
    if not text:
        return ''
    result = []
    chars = iter(text)
    current_char = next(chars)
    count = 1
    for char in chars:
        if char == current_char:
            count += 1
        else:
            yield f'{current_char}{count}'
            current_char = char
            count = 1
    yield f'{current_char}{count}'

def encode_full(text):
    if not text:
        return ''
    return ''.join(run_length_encode(text))

if __name__ == '__main__':
    sample_input = 'AAABBBCCDAA'
    encoded_output = encode_full(sample_input)
    print(encoded_output)