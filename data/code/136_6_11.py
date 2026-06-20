def check_string():
    main_string = "Hello, world!"
    substring1 = "world"
    substring2 = "Python"
    pattern = r"\b\w{5}\b"

    contains_substring1 = substring1 in main_string
    contains_substring2 = substring2 in main_string
    matches_pattern = bool(re.search(pattern, main_string))

    return contains_substring1 and not contains_substring2 or matches_pattern

if __name__ == '__main__':
    result = check_string()
    print(result)