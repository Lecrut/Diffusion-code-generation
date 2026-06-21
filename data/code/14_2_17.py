def are_characters_unique(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string = "hello"
    result = are_characters_unique(sample_string)
    print(result)