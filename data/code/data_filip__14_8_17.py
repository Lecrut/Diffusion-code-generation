def all_characters_distinct(s: str) -> bool:
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample = "abcde"
    print(all_characters_distinct(sample))