def all_characters_distinct(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample1 = "abcde"
    sample2 = "hello"
    print(all_characters_distinct(sample1))
    print(all_characters_distinct(sample2))