def run_length_encode(input_string):
    if not input_string:
        return ""
    
    def generator():
        if not input_string:
            return
        current_char = input_string[0]
        count = 1
        for char in input_string[1:]:
            if char == current_char:
                count += 1
            else:
                yield f"{current_char}{count}"
                current_char = char
                count = 1
        yield f"{current_char}{count}"
    
    return "".join(generator())

if __name__ == '__main__':
    sample_data = "aaabbbcccaaa"
    result = run_length_encode(sample_data)
    print(result)