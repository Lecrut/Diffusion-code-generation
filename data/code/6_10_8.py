def replace_spaces_with_underscores(s):
    return s.replace(" ", "_")

if __name__ == "__main__":
    result = replace_spaces_with_underscores("hello world")
    print(result)