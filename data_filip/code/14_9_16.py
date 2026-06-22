def contains_unique_characters(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "abc"]
    for s in sample_strings:
        result = contains_unique_characters(s)
        print(f"{s}: {result}")