def all_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample = "abcde"
    print(all_unique_characters(sample))