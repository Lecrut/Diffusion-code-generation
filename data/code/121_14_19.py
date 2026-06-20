def compare_strings(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both inputs must be strings.")
    
    return max(s1, s2)

if __name__ == '__main__':
    print(compare_strings("apple", "banana"))