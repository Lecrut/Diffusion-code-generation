def substring_exists(substring, string_list):
    return any(substring in s for s in string_list)

if __name__ == '__main__':
    sample_substring = 'test'
    sample_string_list = ['hello', 'world', 'this is a test']
    print(substring_exists(sample_substring, sample_string_list))