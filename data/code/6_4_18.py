def replace_spaces(s: str) -> str:
    return s.replace(" ", "_")

if __name__ == '__main__':
    result = replace_spaces("hello world foo")
    print(result)