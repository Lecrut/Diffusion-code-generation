def combine_strings(s1: str, s2: str) -> None:
    for c in s1 + s2:
        yield c
if __name__ == '__main__':
    result = list(combine_strings("Hello", "World"))
    print("".join(result))