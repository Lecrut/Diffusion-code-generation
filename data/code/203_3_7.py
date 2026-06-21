def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings.")
    
    return str1 < str2

if __name__ == '__main__':
    result = compare_strings("apple", "banana")
    print(result)