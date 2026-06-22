def trim_whitespace(text: str) -> str:
    start = 0
    length = len(text)
    while start < length and text[start] in " \t\n\r\f\v":
        start += 1
    
    end = length
    while end > start and text[end - 1] in " \t\n\r\f\v":
        end -= 1
    
    return text[start:end]

if __name__ == "__main__":
    sample_string = "   Hello World   "
    result = trim_whitespace(sample_string)
    print(result)
    
    another_sample = "\t\n\r\t\tPython\t\r\n"
    result_two = trim_whitespace(another_sample)
    print(result_two)
    
    empty_sample = "   "
    result_three = trim_whitespace(empty_sample)
    print(repr(result_three))
    
    no_space_sample = "Clean"
    result_four = trim_whitespace(no_space_sample)
    print(result_four)