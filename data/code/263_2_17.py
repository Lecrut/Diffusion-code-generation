def are_anagrams(str1: str, str2: str) -> bool:
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    result = are_anagrams("listen", "silent")
    print(result)