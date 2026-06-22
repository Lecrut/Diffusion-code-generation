def are_characters_unique(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string = "abcdefg"
    print(are_characters_unique(sample_string))
    sample_string_duplicate = "hello"
    print(are_characters_unique(sample_string_duplicate))