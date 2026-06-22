def are_all_characters_unique(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "hello"
    print(are_all_characters_unique(test_string))
    test_string = "world"
    print(are_all_characters_unique(test_string))