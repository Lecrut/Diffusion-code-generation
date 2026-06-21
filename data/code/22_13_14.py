def rle_compress_selective(data):
    if not data:
        return ""
    
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        
        while i + count < n and data[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(str(count))
            result.append(current_char)
        else:
            result.extend([current_char] * count)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    samples = [
        "",
        "a",
        "aa",
        "aaa",
        "aaaa",
        "aabbcc",
        "aaabbbccc",
        "aaabbbaaa",
        "xyzyyyzz",
        "aabbcccddddeeff",
        "hello world",
        "AAAAAAAAAA",
        "abababab",
        "aaabbaaacc",
    ]
    
    for sample in samples:
        compressed = rle_compress_selective(sample)
        print(f"Input: {sample!r}")
        print(f"Compressed: {compressed!r}")
        print()