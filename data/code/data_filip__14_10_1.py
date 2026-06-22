def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_strings = [
        "abcdefg",
        "hello",
        "abcdeff",
        "Python",
        ""
    ]
    for s in sample_strings:
        print(has_unique_characters(s))