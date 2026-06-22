def compress_sequence():
    sequence = 'zzzzzxyyy'
    result = []
    if not sequence:
        return result
    
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return result

if __name__ == '__main__':
    compressed = compress_sequence()
    print(compressed)