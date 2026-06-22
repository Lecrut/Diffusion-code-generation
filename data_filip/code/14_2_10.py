def are_all_chars_unique(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample = "hello"
    print(are_all_chars_unique(sample))