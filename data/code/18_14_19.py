def run_length_encode(input_string):
    if not input_string:
        return
    char_count = 0
    current_char = None
    for char in input_string:
        if char == current_char:
            char_count += 1
        else:
            if current_char is not None:
                yield (current_char, char_count)
            current_char = char
            char_count = 1
    if current_char is not None:
        yield (current_char, char_count)

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = list(run_length_encode(sample_input))
    print(result)