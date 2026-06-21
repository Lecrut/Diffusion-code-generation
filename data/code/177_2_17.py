def split_non_empty_tokens(s):
    return [token for token in s.split() if token]

if __name__ == '__main__':
    sample_string = "  This   is  a test string with   multiple spaces.  "
    print(split_non_empty_tokens(sample_string))