import re

def escape_rle_encode(data: str) -> str:
    if not data:
        return ''
    result = []
    i = 0
    n = len(data)
    while i < n:
        current_char = data[i]
        run_length = 1
        while i + run_length < n and data[i + run_length] == current_char:
            run_length += 1
        needs_escape = current_char in '0123456789\\'
        if run_length > 1:
            if needs_escape:
                result.append(str(run_length))
                result.append('\\')
                result.append(current_char)
            else:
                result.append(str(run_length))
                result.append(current_char)
        elif needs_escape:
            result.append('\\')
            result.append(current_char)
        else:
            result.append(current_char)
        i += run_length
    return ''.join(result)

def escape_rle_decode(encoded: str) -> str:
    if not encoded:
        return ''
    result = []
    i = 0
    n = len(encoded)
    while i < n:
        char = encoded[i]
        if char == '\\':
            if i + 1 < n:
                next_char = encoded[i + 1]
                result.append(next_char)
                i += 2
            else:
                result.append(char)
                i += 1
        elif char.isdigit():
            j = i
            while j < n and encoded[j].isdigit():
                j += 1
            count_str = encoded[i:j]
            count = int(count_str)
            if j < n:
                run_char = encoded[j]
                result.append(run_char * count)
                i = j + 1
            else:
                result.append(count_str)
                i = j
        else:
            result.append(char)
            i += 1
    return ''.join(result)
if __name__ == '__main__':
    original_text = 'AAABBC111D\\E'
    encoded_value = escape_rle_encode(original_text)
    decoded_value = escape_rle_decode(encoded_value)
    print(f'Original: {original_text}')
    print(f'Encoded: {encoded_value}')
    print(f'Decoded: {decoded_value}')
    print(f'Match: {original_text == decoded_value}')