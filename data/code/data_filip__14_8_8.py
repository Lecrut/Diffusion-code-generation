def all_characters_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    print(all_characters_distinct("abcdef"))
    print(all_characters_distinct("hello"))