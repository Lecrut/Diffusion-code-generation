def rle_decompress(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        if i + 1 < n and compressed[i].isdigit():
            count_str = ""
            while i < n and compressed[i].isdigit():
                count_str += compressed[i]
                i += 1
            
            if count_str:
                count = int(count_str)
                if i < n:
                    char_to_repeat = compressed[i]
                    result.append(char_to_repeat * count)
                    i += 1
                else:
                    raise ValueError("Invalid RLE format: count without character")
            else:
                raise ValueError("Invalid RLE format: digit without following character")
        elif not compressed[i].isdigit():
            result.append(compressed[i])
            i += 1
        else:
            i += 1
            
    return "".join(result)

if __name__ == "__main__":
    sample_input = "4a3b2c1d5e"
    decompressed_output = rle_decompress(sample_input)
    print(decompressed_output)