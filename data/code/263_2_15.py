def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    result = are_anagrams("listen", "silent")
    print(result)