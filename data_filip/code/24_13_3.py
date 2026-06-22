import re
from functools import reduce

def run_length_encode(data: str) -> str:
    if not data:
        return ''
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 3:
                encoded.append(f'{count}{current_char}')
            elif count > 1:
                encoded.append(f'{count}{current_char}')
            else:
                encoded.append(current_char)
            current_char = char
            count = 1
    if count > 3:
        encoded.append(f'{count}{current_char}')
    elif count > 1:
        encoded.append(f'{count}{current_char}')
    else:
        encoded.append(current_char)
    return ''.join(encoded)

def run_length_decode(data: str) -> str:
    if not data:
        return ''
    decoded = []
    length = len(data)
    i = 0
    while i < length:
        char = data[i]
        if char.isdigit():
            j = i
            while j < length and data[j].isdigit():
                j += 1
            count = int(data[i:j])
            if j < length:
                next_char = data[j]
                decoded.append(next_char * count)
                i = j + 1
            else:
                decoded.append(char)
                i += 1
        else:
            decoded.append(char)
            i += 1
    return ''.join(decoded)
if __name__ == '__main__':
    original_text = 'AAABBBCCD'
    encoded_result = run_length_encode(original_text)
    decoded_result = run_length_decode(encoded_result)
    print(f'Original: {original_text}')
    print(f'Encoded: {encoded_result}')
    print(f'Decoded: {decoded_result}')
    print(f'Match: {original_text == decoded_result}')
    sample_text = 'WWWWWWWWWWWWBWWWW'
    encoded_sample = run_length_encode(sample_text)
    decoded_sample = run_length_decode(encoded_sample)
    print(f'Sample Original: {sample_text}')
    print(f'Sample Encoded: {encoded_sample}')
    print(f'Sample Decoded: {decoded_sample}')