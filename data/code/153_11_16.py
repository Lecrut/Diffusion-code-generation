def substring_exists(substring, string_list):
    return substring in set(string_list)

if __name__ == '__main__':
    sample_substring = 'example'
    sample_string_list = ['test', 'sample', 'example', 'data']
    print(substring_exists(sample_substring, sample_string_list))