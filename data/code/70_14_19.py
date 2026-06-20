def get_first_last_chars(s):
    if not isinstance(s, str) or len(s) < 1:
        return None
    first_char = s[0]
    last_char = s[-1]
    return first_char, last_char

if __name__ == '__main__':
    sample_string = "example"
    result = get_first_last_chars(sample_string)
    if result:
        print(f"First character: {result[0]}")
        print(f"Last character: {result[1]}")