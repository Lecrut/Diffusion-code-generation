def spaces_to_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample = "hello world"
    print(spaces_to_underscores(sample))