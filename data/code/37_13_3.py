def join_strings_fstring(str1, str2):
    return f"{str1} and {str2}"
if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    result = join_strings_fstring(string_a, string_b)
    print(result)