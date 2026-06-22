from typing import Tuple, List

def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ''
    encoded_chars: List[str] = []
    current_char: str = input_string[0]
    count: int = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f'{count}{current_char}')
            current_char = char
            count = 1
    encoded_chars.append(f'{count}{current_char}')
    return ''.join(encoded_chars)

def run_length_decode(input_string: str) -> str:
    if not input_string:
        return ''
    decoded_chars: List[str] = []
    i: int = 0
    n: int = len(input_string)
    while i < n:
        num_str: List[str] = []
        while i < n and input_string[i].isdigit():
            num_str.append(input_string[i])
            i += 1
        if not num_str:
            break
        count: int = int(''.join(num_str))
        if i < n:
            decoded_chars.append(input_string[i] * count)
            i += 1
    return ''.join(decoded_chars)
if __name__ == '__main__':
    original_text: str = 'AAABBBCCD'
    encoded_text: str = run_length_encode(original_text)
    print(encoded_text)
    decoded_text: str = run_length_decode(encoded_text)
    print(decoded_text)