def compress_rle(digits: str) -> str:
    if not digits:
        return ""
    
    result = []
    current_char = digits[0]
    count = 1
    
    for i in range(1, len(digits)):
        if digits[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = digits[i]
            count = 1
            
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sequence = "11222333344444"
    compressed = compress_rle(sequence)
    print(compressed)