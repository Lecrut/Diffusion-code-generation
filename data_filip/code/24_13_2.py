def rle_encode(data):
    if not data:
        return ''
    encoded_parts = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded_parts.append(str(count) + current_char)
    return ''.join(encoded_parts)

def rle_decode(encoded_data):
    if not encoded_data:
        return ''
    decoded_parts = []
    count_str = ''
    i = 0
    while i < len(encoded_data):
        if encoded_data[i].isdigit():
            count_str += encoded_data[i]
        else:
            if count_str:
                count = int(count_str)
                decoded_parts.append(encoded_data[i] * count)
                count_str = ''
        i += 1
    return ''.join(decoded_parts)

if __name__ == '__main__':
    sample_string = 'AAABBBCCDAA'
    encoded = rle_encode(sample_string)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)
    empty_string = ''
    encoded_empty = rle_encode(empty_string)
    print(encoded_empty)
    decoded_empty = rle_decode(encoded_empty)
    print(decoded_empty)
    single_char = 'A'
    encoded_single = rle_encode(single_char)
    print(encoded_single)
    decoded_single = rle_decode(encoded_single)
    print(decoded_single)
    mixed_string = 'ABC'
    encoded_mixed = rle_encode(mixed_string)
    print(encoded_mixed)
    decoded_mixed = rle_decode(encoded_mixed)
    print(decoded_mixed)
    long_run = 'A' * 100
    encoded_long = rle_encode(long_run)
    print(encoded_long)
    decoded_long = rle_decode(encoded_long)
    print(decoded_long)
    complex_string = 'AABBCCDDEEFFF'
    encoded_complex = rle_encode(complex_string)
    print(encoded_complex)
    decoded_complex = rle_decode(encoded_complex)
    print(decoded_complex)
    numbers_string = '112233'
    encoded_numbers = rle_encode(numbers_string)
    print(encoded_numbers)
    decoded_numbers = rle_decode(encoded_numbers)
    print(decoded_numbers)
    special_chars = '!!@@##'
    encoded_special = rle_encode(special_chars)
    print(encoded_special)
    decoded_special = rle_decode(encoded_special)
    print(decoded_special)
    spaces_string = '   a  b   '
    encoded_spaces = rle_encode(spaces_string)
    print(encoded_spaces)
    decoded_spaces = rle_decode(encoded_spaces)
    print(decoded_spaces)
    unicode_string = 'こんにちは'
    encoded_unicode = rle_encode(unicode_string)
    print(encoded_unicode)
    decoded_unicode = rle_decode(encoded_unicode)
    print(decoded_unicode)
    emoji_string = '😀😀😂😂😂'
    encoded_emoji = rle_encode(emoji_string)
    print(encoded_emoji)
    decoded_emoji = rle_decode(encoded_emoji)
    print(decoded_emoji)
    large_input = 'A' * 10000 + 'B' * 5000 + 'C' * 3000
    encoded_large = rle_encode(large_input)
    print(encoded_large)
    decoded_large = rle_decode(encoded_large)
    print(decoded_large == large_input)