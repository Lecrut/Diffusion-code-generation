def compress_sequence(digits):
    if not digits:
        return ""
    
    result = []
    current_char = digits[0]
    count = 1
    
    for i in range(1, len(digits)):
        if digits[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = digits[i]
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "111222233344"
    compressed_output = compress_sequence(sample_input)
    print(compressed_output)