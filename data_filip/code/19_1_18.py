def decode_rle(encoded: str) -> str:
    if not encoded:
        return ''
    result = []
    i = 0
    n = len(encoded)
    while i < n:
        char = encoded[i]
        if char.isdigit():
            j = i
            while j < n and encoded[j].isdigit():
                j += 1
            count = int(encoded[i:j])
            if j >= n:
                raise ValueError('Invalid RLE format: digit at end of string without a following character')
            next_char = encoded[j]
            if not next_char.isalpha():
                raise ValueError('Invalid RLE format: non-letter character following count')
            result.append(next_char * count)
            i = j + 1
        elif char.isalpha():
            result.append(char)
            i += 1
        else:
            raise ValueError('Invalid character in RLE string')
    return ''.join(result)
if __name__ == '__main__':
    sample_input = '2a3b4c1d2e'
    decoded_output = decode_rle(sample_input)
    print(decoded_output)