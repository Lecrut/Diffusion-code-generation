def all_characters_distinct(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample = "abcdef"
    print(all_characters_distinct(sample))