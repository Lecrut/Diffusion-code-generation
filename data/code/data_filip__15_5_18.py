def compress_string(text):
    if not text:
        return ""
    
    current_char = text[0]
    run_length = 1
    segments = []
    
    for index in range(1, len(text)):
        next_char = text[index]
        if next_char == current_char:
            run_length += 1
        else:
            segment_fragment = current_char + str(run_length)
            segments.append(segment_fragment)
            current_char = next_char
            run_length = 1
    
    final_fragment = current_char + str(run_length)
    segments.append(final_fragment)
    compressed_output = "".join(segments)
    return compressed_output

if __name__ == '__main__':
    test_string = "aaaabbbccdd"
    result_value = compress_string(test_string)
    print(result_value)