def are_all_characters_distinct(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    print(are_all_characters_distinct("abcde"))
    print(are_all_characters_distinct("hello"))