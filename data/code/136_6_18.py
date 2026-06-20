def check_string():
    main_string = "Hello, world!"
    substring1 = "world"
    substring2 = "Python"
    pattern = r"\bwo\w+"

    contains_substring1 = substring1 in main_string
    contains_substring2 = substring2 in main_string
    matches_pattern = re.search(pattern, main_string) is not None

    return contains_substring1 and contains_substring2 or matches_pattern

if __name__ == '__main__':
    print(check_string())