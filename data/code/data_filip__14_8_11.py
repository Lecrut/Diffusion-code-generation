def are_all_characters_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample1 = "hello"
    sample2 = "world"
    print(are_all_characters_distinct(sample1))
    print(are_all_characters_distinct(sample2))