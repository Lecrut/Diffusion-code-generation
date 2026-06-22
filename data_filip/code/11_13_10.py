def find_repeated_chars(s):
    return [c for c in sorted(set(s)) if s.count(c) > 1]

if __name__ == '__main__':
    sample_string = "hello world"
    print(find_repeated_chars(sample_string))