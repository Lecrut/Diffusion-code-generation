def are_all_characters_distinct(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample1 = "abcdefg"
    sample2 = "hello"
    print(are_all_characters_distinct(sample1))
    print(are_all_characters_distinct(sample2))