def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError('Both inputs must be strings')
    string_map = {'prefix': str1, 'suffix': str2}
    combined_result = string_map['prefix'] + string_map['suffix']
    return combined_result
if __name__ == '__main__':
    result = combine_strings('Hello, ', 'World!')
    print(result)