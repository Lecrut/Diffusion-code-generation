def word_length_dict(text: str) -> dict[int, list[str]]:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    length_dict = {}
    
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    
    return length_dict

if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, how are you?"
    sample_string_2 = "  Multiple   spaces\tand\nnewlines\nwith punctuation... "
    sample_string_3 = "Word123-with_hyphens and $symbols."
    sample_string_4 = ""
    sample_string_5 = "OnlyWords"
    
    print(f"Input: '{sample_string_1}'")
    result_1 = word_length_dict(sample_string_1)
    print(f"Output: {result_1}\n")
    
    print(f"Input: '{sample_string_2}'")
    result_2 = word_length_dict(sample_string_2)
    print(f"Output: {result_2}\n")
    
    print(f"Input: '{sample_string_3}'")
    result_3 = word_length_dict(sample_string_3)
    print(f"Output: {result_3}\n")
    
    print(f"Input: '{sample_string_4}'")
    result_4 = word_length_dict(sample_string_4)
    print(f"Output: {result_4}\n")
    
    print(f"Input: '{sample_string_5}'")
    result_5 = word_length_dict(sample_string_5)
    print(f"Output: {result_5}\n")