def run_length_encode(input_string):
    if not input_string:
        return ""
    
    def generator():
        current_char = input_string[0]
        count = 1
        for char in input_string[1:]:
            if char == current_char:
                count += 1
            else:
                yield str(count) + current_char
                current_char = char
                count = 1
        yield str(count) + current_char
    
    return "".join(generator())

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)