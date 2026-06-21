def has_duplicates(text):
    return len(text) != len(set(text))

if __name__ == '__main__':
    sample1 = "hello"
    sample2 = "world"
    print(has_duplicates(sample1))
    print(has_duplicates(sample2))