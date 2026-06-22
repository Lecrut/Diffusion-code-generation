def sort_strings_alphabetically(strings):
    def case_insensitive_key(s):
        return (s.lower(), s)
    
    sorted_list = sorted(strings, key=case_insensitive_key)
    return sorted_list

if __name__ == '__main__':
    sample_data = ["Grape", "apple", "orange", "Banana", "cherry"]
    result = sort_strings_alphabetically(sample_data)
    print(result)