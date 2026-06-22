def rle_encode(text):
    if not text:
        return ''
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return ''.join(encoded)

if __name__ == '__main__':
    sample_text = 'aaabbcdda'
    result = rle_encode(sample_text)
    print(result)
    
    empty_text = ''
    empty_result = rle_encode(empty_text)
    print(repr(empty_result))
    
    single_char = 'z'
    single_result = rle_encode(single_char)
    print(single_result)