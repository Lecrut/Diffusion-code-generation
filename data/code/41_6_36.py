def to_title_case(strings):
    return [s.title() for s in strings]

if __name__ == '__main__':
    input_strings = ["the quick brown fox", "jumps OVER the lazy dog", "PYTHON programming"]
    converted_strings = to_title_case(input_strings)
    print(converted_strings)