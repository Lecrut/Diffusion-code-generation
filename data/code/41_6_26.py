def convert_to_title_case(strings):
    return [s.title() for s in strings]

if __name__ == '__main__':
    SAMPLE_STRINGS = ["hello world", "PYTHON programming", "this is a TEST"]
    title_cased_strings = convert_to_title_case(SAMPLE_STRINGS)
    print(title_cased_strings)