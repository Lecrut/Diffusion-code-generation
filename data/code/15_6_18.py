def compress_sequence(input_str: str) -> list:
    if not input_str:
        return []
    
    result = []
    current_char = input_str[0]
    count = 1
    
    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return result

if __name__ == '__main__':
    sample = 'zzzzzxyyy'
    compressed = compress_sequence(sample)
    print(compressed)