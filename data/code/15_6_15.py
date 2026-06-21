def compress_sequence(source):
    if not source:
        return []
    
    result = []
    current_char = source[0]
    count = 1
    
    for char in source[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'zzzzzxyyy'
    compressed_output = compress_sequence(sample_input)
    print(compressed_output)