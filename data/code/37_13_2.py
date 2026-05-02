def join_strings_fstring(str1, str2):
    result = f"{str1} and {str2}"
    return result
if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    joined_string = join_strings_fstring(string_a, string_b)
    print(joined_string)