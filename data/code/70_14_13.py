def get_first_last_chars(s):
    return (s[0], s[-1])

if __name__ == '__main__':
    sample = "Hello, World!"
    print(get_first_last_chars(sample))