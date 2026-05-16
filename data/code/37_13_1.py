def join_strings(str1, str2):
    result = f"{str1}---{str2}"
    return result
if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    joined_string = join_strings(string_a, string_b)
    print(joined_string)