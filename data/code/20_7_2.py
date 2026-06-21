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
            result.append(f"{current_char}{count}")
            current_char = digits[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_digits = "111222333344444"
    compressed = compress_sequence(sample_digits)
    print(compressed)