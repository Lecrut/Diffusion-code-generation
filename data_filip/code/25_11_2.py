def decompress_run_length(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    length = len(encoded)
    
    while i < length:
        if not encoded[i].isdigit():
            result.append(encoded[i])
            i += 1
        else:
            j = i
            while j < length and encoded[j].isdigit():
                j += 1
            count_str = encoded[i:j]
            count = int(count_str)
            
            if j < length:
                char = encoded[j]
                result.append(char * count)
                i = j + 1
            else:
                i = j
                
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a3b2c1d4"
    output = decompress_run_length(sample_input)
    print(output)