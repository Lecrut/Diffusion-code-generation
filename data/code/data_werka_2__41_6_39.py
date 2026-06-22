def convert_to_title_case(strings):
    def title_case(s):
        return s.title()
    
    return [title_case(s) for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    title_cased_strings = convert_to_title_case(sample_strings)
    print(title_cased_strings)