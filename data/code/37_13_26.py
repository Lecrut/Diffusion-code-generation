def join_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings")
    
    result = str1 + " and " + str2
    return result

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    try:
        joined_string = join_strings(string_a, string_b)
        print(joined_string)
    except ValueError as e:
        print(e)