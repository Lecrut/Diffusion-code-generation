def remove_internal_spaces(strings):
    def strip_string(s):
        return s.replace(' ', '')
    
    result = []
    for string in strings:
        stripped_string = strip_string(string)
        result.append(stripped_string)
    
    return result

if __name__ == '__main__':
    sample_strings = ["example sentence", "another test case", "space removal"]
    processed_strings = remove_internal_spaces(sample_strings)
    print(processed_strings)