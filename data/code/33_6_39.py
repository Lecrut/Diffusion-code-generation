def remove_internal_spaces(strings):
    def strip_spaces(s):
        return s.replace(' ', '')
    
    return [strip_spaces(s) for s in strings]

if __name__ == '__main__':
    SAMPLE_STRINGS = ["hello world", "this is a test", "remove spaces here"]
    result = remove_internal_spaces(SAMPLE_STRINGS)
    print(result)