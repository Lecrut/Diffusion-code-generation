RLE_COUNT_PREFIX = True

def compress_run_length(text):
    if not text:
        return ""
    
    segments = []
    first_char = text[0]
    run_length = 1
    
    for index in range(1, len(text)):
        current_char = text[index]
        if current_char == first_char:
            run_length += 1
        else:
            segments.append(str(run_length) + first_char)
            first_char = current_char
            run_length = 1
            
    segments.append(str(run_length) + first_char)
    return "".join(segments)

if __name__ == '__main__':
    sample_input = "XYYYZZZABBBCC"
    result = compress_run_length(sample_input)
    print(result)