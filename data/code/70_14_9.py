def get_first_last_char(s):
    if not s:
        return None, None
    first = s[0]
    last = s[-1]
    return first, last

if __name__ == '__main__':
    sample_string = "hello"
    first_char, last_char = get_first_last_char(sample_string)
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")