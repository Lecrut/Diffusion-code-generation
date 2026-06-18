def merge_strings(s1: str, s2: str) -> None:
    for char in (s1 + s2):
        yield char
if __name__ == '__main__':
    result = list(merge_strings("Hello", "World"))
    print("".join(result))