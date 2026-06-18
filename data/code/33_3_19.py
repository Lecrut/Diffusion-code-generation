def remove_spaces(s):
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Code Golf in Python",
        "",
        "   Multiple     Spaces   ",
        "NoSpacesHere"
    ]
    
    for case in test_cases:
        print(f"Input: {case!r} -> Output: {remove_spaces(case)!r}")