def run_length_encode(data: str) -> str:
    if not data:
        return ''
    encoded = []
    count = 1
    current_char = data[0]
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f'{count}{current_char}')
            current_char = char
            count = 1
    encoded.append(f'{count}{current_char}')
    return ''.join(encoded)

def run_length_decode(data: str) -> str:
    if not data:
        return ''
    decoded = []
    count_str = []
    for char in data:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int(''.join(count_str))
            decoded.append(char * count)
            count_str = []
    return ''.join(decoded)
if __name__ == '__main__':
    sample_text = 'aabcccccaaa'
    encoded_result = run_length_encode(sample_text)
    print(f'Encoded: {encoded_result}')
    decoded_result = run_length_decode(encoded_result)
    print(f'Decoded: {decoded_result}')
    is_round_trip_correct = sample_text == decoded_result
    print(f'Round-trip correct: {is_round_trip_correct}')
    empty_encoded = run_length_encode('')
    print(f"Empty encoded: '{empty_encoded}'")
    single_encoded = run_length_encode('z')
    print(f'Single char encoded: {single_encoded}')
    single_decoded = run_length_decode(single_encoded)
    print(f'Single char decoded: {single_decoded}')