def decompress_run_length(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    current_number = []
    
    for char in encoded:
        if char.isdigit():
            current_number.append(char)
        else:
            if current_number:
                count = int("".join(current_number))
                current_number = []
                result.append(char * count)
            else:
                result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_encoded = "A3B2C4"
    uncompressed = decompress_run_length(sample_encoded)
    print(uncompressed)