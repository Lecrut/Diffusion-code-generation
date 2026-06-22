def are_anagrams(str1: str, str2: str) -> bool:

    def is_valid_string(s: str) -> bool:
        return isinstance(s, str) and s.isalpha()
    if not (is_valid_string(str1) and is_valid_string(str2)):
        raise ValueError('Both inputs must be non-empty alphabetic strings.')
    return sorted(str1) == sorted(str2)
if __name__ == '__main__':
    print(are_anagrams('listen', 'silent'))
    print(are_anagrams('hello', 'world'))