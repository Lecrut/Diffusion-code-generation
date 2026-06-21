def contains_substring(sub, lst):
    return any(sub in s for s in lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    substring = 'an'
    print(contains_substring(substring, sample_list))