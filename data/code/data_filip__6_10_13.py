def replace_spaces_with_underscores(input_string: str) -> str:
    return input_string.replace(' ', '_')
if __name__ == '__main__':
    sample_inputs = ['Hello World', 'Python is great', '   multiple   spaces   ', 'NoSpacesHere', '', '   ', 'a b c d e']
    for sample in sample_inputs:
        result = replace_spaces_with_underscores(sample)
        print(f"Input: '{sample}' -> Output: '{result}'")