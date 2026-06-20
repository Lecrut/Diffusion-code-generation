def capitalize_first(string):
    if not string:
        return string
    return string[0].upper() + string[1:].lower()

if __name__ == '__main__':
    test_cases = ["hELLO", "wORLd", "pYTHON", "a", "A", ""]
    for s in test_cases:
        result = capitalize_first(s)
        print(result)