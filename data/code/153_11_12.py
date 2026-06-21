def substring_in_list(substring, string_list):
    return substring in set(string_list)

if __name__ == '__main__':
    sample_substring = 'test'
    sample_string_list = ['hello', 'world', 'this', 'is', 'a', 'test']
    print(substring_in_list(sample_substring, sample_string_list))