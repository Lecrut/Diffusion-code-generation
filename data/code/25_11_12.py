def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ''
    
    result_parts = []
    num_buffer = []
    
    for char in encoded:
        if char.isdigit():
            num_buffer.append(char)
        else:
            if num_buffer:
                count = int(''.join(num_buffer))
                result_parts.append(char * count)
                num_buffer.clear()
            else:
                result_parts.append(char)
    
    if num_buffer:
        count = int(''.join(num_buffer))
        result_parts.append('' * count)
        
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_encoded = '3a1b1c'
    original = decompress_rle(sample_encoded)
    print(original)
    
    sample_encoded2 = '2b'
    original2 = decompress_rle(sample_encoded2)
    print(original2)
    
    sample_encoded3 = ''
    original3 = decompress_rle(sample_encoded3)
    print(original3)