def check_string():
    target = "Hello, world!"
    substring1 = "world"
    substring2 = "Python"
    pattern = r"\b\w{5}\b"

    contains_substring1 = substring1 in target
    contains_substring2 = substring2 in target
    matches_pattern = bool(re.search(pattern, target))

    return contains_substring1 and (not contains_substring2) or matches_pattern

if __name__ == '__main__':
    print(check_string())