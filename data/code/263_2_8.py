def are_anagrams(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError('Both inputs must be strings')
    return sorted(str1) == sorted(str2)
if __name__ == '__main__':
    print(are_anagrams('listen', 'silent'))
    print(are_anagrams('hello', 'world'))