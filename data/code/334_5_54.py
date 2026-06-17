def combined_generator(s1: str, s2: str) -> str:
    result = []
    for char in (s1 + s2):
        yield char
if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World!"
    gen = combined_generator(string_a, string_b)
    print("".join(gen))