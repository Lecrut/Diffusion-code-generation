def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
if __name__ == '__main__':
    print(are_anagrams('listen', 'silent'))
    print(are_anagrams('hello', 'billion'))