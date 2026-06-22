def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return str1 + str2

if __name__ == '__main__':
    try:
        string1 = "Good evening, "
        string2 = "Universe!"
        result = combine_strings(string1, string2)
        print(result)
    except ValueError as e:
        print(e)