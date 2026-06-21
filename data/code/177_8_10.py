def split_text(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample_input = "this is a test string"
    result = split_text(sample_input)
    print(f"Input: '{sample_input}'")
    print(f"Output: {result}")
    sample_input_2 = "multiple   spaces here"
    result_2 = split_text(sample_input_2)
    print(f"Input: '{sample_input_2}'")
    print(f"Output: {result_2}")
    sample_input_3 = "singleword"
    result_3 = split_text(sample_input_3)
    print(f"Input: '{sample_input_3}'")
    print(f"Output: {result_3}")