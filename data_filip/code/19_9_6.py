import re

def enhanced_rle_encode(data):
    if not data:
        return ""
    escaped = _escape_special(data)
    return _run_length_encode(escaped)

def enhanced_rle_decode(data):
    decoded_escaped = _run_length_decode(data)
    return _unescape_special(decoded_escaped)

_ESCAPE_CHAR = '\\'
_SPECIAL_CHARS = '\\ N'

_ESCAPE_MAP = {
    '\\': '\\\\',
    'N': '\\N'
}

_UNESCAPE_MAP = {
    '\\\\': '\\',
    '\\N': 'N'
}

def _escape_special(data):
    result = []
    for char in data:
        if char in _ESCAPE_MAP:
            result.append(_ESCAPE_MAP[char])
        else:
            result.append(char)
    return "".join(result)

def _unescape_special(data):
    result = []
    i = 0
    while i < len(data):
        if i + 1 < len(data) and data[i] == _ESCAPE_CHAR:
            pair = data[i:i+2]
            if pair in _UNESCAPE_MAP:
                result.append(_UNESCAPE_MAP[pair])
                i += 2
                continue
            else:
                result.append(data[i])
                i += 1
        else:
            result.append(data[i])
            i += 1
    return "".join(result)

def _run_length_encode(data):
    if not data:
        return ""
    encoded = []
    i = 0
    while i < len(data):
        char = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == char:
            count += 1
        if count == 1 and char.isdigit():
            encoded.append(escape_digit(char))
        elif count > 1:
            encoded.append(str(count) + char)
        else:
            encoded.append(char)
        i += count
    return "".join(encoded)

def _run_length_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        if data[i] == _ESCAPE_CHAR and i + 1 < len(data) and data[i+1] == 'd':
            decoded.append(data[i+2])
            i += 3
        elif data[i].isdigit():
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            if i < len(data):
                count = int(num_str)
                char = data[i]
                decoded.append(char * count)
                i += 1
            else:
                decoded.append(num_str)
        else:
            decoded.append(data[i])
            i += 1
    return "".join(decoded)

def escape_digit(char):
    return '\\d' + char

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA1111NN"
    encoded = enhanced_rle_encode(sample_data)
    print(encoded)
    decoded = enhanced_rle_decode(encoded)
    print(decoded)
    print(sample_data == decoded)
    sample_data2 = "Hello World"
    encoded2 = enhanced_rle_encode(sample_data2)
    print(encoded2)
    decoded2 = enhanced_rle_decode(encoded2)
    print(decoded2)
    print(sample_data2 == decoded2)
    sample_data3 = "12345"
    encoded3 = enhanced_rle_encode(sample_data3)
    print(encoded3)
    decoded3 = enhanced_rle_decode(encoded3)
    print(decoded3)
    print(sample_data3 == decoded3)