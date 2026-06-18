def combined_generator(s1: str, s2: str):
    for char in (s1 + s2):
        yield char
if __name__ == '__main__':
    result = list(combined_generator("Hello", "World"))
    print(result)