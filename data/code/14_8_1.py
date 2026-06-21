def all_unique_characters(text):
    return len(text) == len(set(text))

if __name__ == '__main__':
    sample_1 = "abcdef"
    sample_2 = "hello"
    print(all_unique_characters(sample_1))
    print(all_unique_characters(sample_2))