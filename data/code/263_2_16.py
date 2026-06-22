def are_anagrams(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    result = are_anagrams("listen", "silent")
    print(result)