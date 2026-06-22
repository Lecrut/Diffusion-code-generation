def clean_strings(string_list):
    return [s.strip() for s in string_list]

if __name__ == '__main__':
    sample = [
        "  hello world  ",
        "  foo  bar  ",
        "    ",
        "no_whitespace",
        " trailing only",
        "leading only "
    ]
    cleaned = clean_strings(sample)
    print(cleaned)