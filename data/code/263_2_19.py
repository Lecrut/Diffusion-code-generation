def are_anagrams(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2

if __name__ == '__main__':
    sample_str1 = "listen"
    sample_str2 = "silent"
    print(are_anagrams(sample_str1, sample_str2))