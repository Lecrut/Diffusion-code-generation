def remove_spaces(s):
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  multiple   spaces  ",
        "",
        "No spaces here"
    ]
    for case in test_cases:
        print(f"{case!r} -> {remove_spaces(case)!r}")