def has_repeated_letters(s):
    return len(set(s)) != len(s)

if __name__ == '__main__':
    sample_string = "programming"
    print(has_repeated_letters(sample_string))