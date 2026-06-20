def clean_strings(string_list):
    return [s.strip() for s in string_list]

if __name__ == '__main__':
    sample = [
        "  hello  ",
        "\tworld\n",
        "  python  ",
        "  ",
        "no_extra_space"
    ]
    print(clean_strings(sample))