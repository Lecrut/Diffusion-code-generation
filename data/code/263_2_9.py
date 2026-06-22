def are_anagrams(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    sample_str1 = "listen"
    sample_str2 = "silent"
    result = are_anagrams(sample_str1, sample_str2)
    print(result)