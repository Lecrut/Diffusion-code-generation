def run_length_encode(input_str):
    if not input_str:
        return
    count = 0
    previous_char = None
    for char in input_str:
        if char == previous_char:
            count += 1
        else:
            if previous_char is not None:
                yield (previous_char, count)
            previous_char = char
            count = 1
    if previous_char is not None:
        yield (previous_char, count)

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = list(run_length_encode(sample_input))
    print(result)