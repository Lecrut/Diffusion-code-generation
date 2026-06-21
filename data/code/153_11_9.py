def substring_in_list(substring, string_list):
    return set(string_list).issuperset({substring})

if __name__ == '__main__':
    sample_substring = 'test'
    sample_string_list = ['hello', 'world', 'test', 'python']
    print(substring_in_list(sample_substring, sample_string_list))