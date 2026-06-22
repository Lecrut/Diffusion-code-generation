def sort_strings_alphabetically(strings):
    LOWERCASE_KEY_INDEX = 0
    CASE_SENSITIVE_KEY_INDEX = 1
    
    def key_function(s):
        return (s.lower(), s)
    
    return sorted(strings, key=key_function)

if __name__ == '__main__':
    SAMPLE_VALUES = ["banana", "Apple", "cherry", "date", "Elderberry"]
    SORTED_VALUES = sort_strings_alphabetically(SAMPLE_VALUES)
    print(SORTED_VALUES)