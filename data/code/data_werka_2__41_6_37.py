def convert_to_title_case(strings):
    def title_case_string(s):
        return s.title()
    
    return [title_case_string(s) for s in strings]

if __name__ == '__main__':
    SAMPLE_STRINGS = ["hello world", "PYTHON programming", "this is a TEST"]
    TITLE_CASED_STRINGS = convert_to_title_case(SAMPLE_STRINGS)
    print(TITLE_CASED_STRINGS)