def convert_spaces(s):
    return s.replace(" ", "_")

if __name__ == '__main__':
    result = convert_spaces("hello world foo bar")
    print(result)