def check_string():
    main_string = "Hello, world!"
    substring_1 = "world"
    substring_2 = "Python"
    pattern = r"\b\w{5}\b"

    contains_substring_1 = substring_1 in main_string
    contains_substring_2 = substring_2 in main_string
    matches_pattern = bool(re.search(pattern, main_string))

    return contains_substring_1 or contains_substring_2 or matches_pattern

if __name__ == '__main__':
    result = check_string()
    print(result)