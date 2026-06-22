def run_length_encode_digits(digit_string):
    if not digit_string:
        return ""
    
    encoded_parts = []
    current_char = digit_string[0]
    count = 1
    
    for i in range(1, len(digit_string)):
        if digit_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = digit_string[i]
            count = 1
    
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_digits = "11223334444445566677777788999"
    result = run_length_encode_digits(sample_digits)
    print(result)