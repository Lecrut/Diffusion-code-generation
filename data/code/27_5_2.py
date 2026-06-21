def rle_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    count = 1
    
    padded = s + '\0'
    
    for current, nxt in zip(s, padded):
        if current == nxt:
            count += 1
        else:
            encoded_parts.append(current)
            if count > 1:
                encoded_parts.append(str(count))
            count = 1
            
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    result = rle_encode(sample_input)
    print(result)