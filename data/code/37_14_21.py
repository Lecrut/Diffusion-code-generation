def concatenate_strings(str1, str2):
    result = str1
    result += str2
    return result

if __name__ == '__main__':
    s1 = "Hello, "
    s2 = "World!"
    print(concatenate_strings(s1, s2))