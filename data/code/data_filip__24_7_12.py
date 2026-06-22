def compress_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(f"{data[i - 1]}{count}")
            count = 1
    
    result.append(f"{data[-1]}{count}")
    return "".join(result)

def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    
    while i < len(encoded):
        if i + 1 >= len(encoded):
            break
        
        char = encoded[i]
        count_str = ""
        i += 1
        
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "0011100"
    compressed = compress_rle(sample_input)
    decompressed = decompress_rle(compressed)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    
    edge_cases = ["", "1", "111111", "010101"]
    for case in edge_cases:
        c = compress_rle(case)
        d = decompress_rle(c)
        print(f"Case '{case}' -> Compressed: '{c}' -> Decompressed: '{d}'")