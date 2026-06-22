def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string_1 = "hello"
    sample_string_2 = "world"
    print(has_unique_characters(sample_string_1))
    print(has_unique_characters(sample_string_2))