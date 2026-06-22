def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    print(has_unique_characters("abcde"))
    print(has_unique_characters("hello"))
    print(has_unique_characters(""))
    print(has_unique_characters("a"))
    print(has_unique_characters("abcdefg"))
    print(has_unique_characters("abacaba"))