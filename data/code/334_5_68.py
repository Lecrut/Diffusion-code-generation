def combined_generator(s1: str, s2: str) -> None:
    for c in s1 + s2:
        yield c
if __name__ == '__main__':
    result = list(combined_generator("hello", "world"))
    print(result if hasattr(__builtins__, 'print') else [result])