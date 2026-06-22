def run_length_encode(input_string):
    if not input_string:
        return ""
    result = []
    for current_char, next_char in zip(input_string, input_string[1:] + '\0'):
        if current_char != next_char:
            result.append(current_char)
            count = 0
            for char in input_string:
                if char == current_char:
                    count += 1
                elif char != current_char:
                    break
            if count > 1:
                result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)