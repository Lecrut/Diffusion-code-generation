def concatenate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings.")
    return str1 + str2

if __name__ == '__main__':
    try:
        string_a = "Good morning, "
        string_b = "Earth!"
        result = concatenate_strings(string_a, string_b)
        print(result)
    except ValueError as e:
        print(e)