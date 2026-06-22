def compare_string_lengths(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len1 > len2:
        return f"'{str1}' is longer."
    elif len1 < len2:
        return f"'{str2}' is longer."
    else:
        return "Both strings are equal in length."

if __name__ == '__main__':
    print(compare_string_lengths("hello", "world"))
    print(compare_string_lengths("short", "longer string"))
    print(compare_string_lengths("equal", "equal"))