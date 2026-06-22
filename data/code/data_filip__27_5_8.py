def encode_rle_via_zip(data: str) -> str:
    if not data:
        return ""
    
    result_parts = []
    current_char = data[0]
    count = 1
    
    padded_data = data[1:] + '\x00'
    
    for curr, nxt in zip(data, padded_data):
        if curr == nxt:
            count += 1
        else:
            if count > 1:
                result_parts.append(f"{count}{curr}")
            else:
                result_parts.append(curr)
            current_char = nxt
            count = 1
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    encoded_value = encode_rle_via_zip(sample_input)
    print(encoded_value)