def combined_generator(str1: str, str2: str):
    for char in (str1 + str2):
        yield char
if __name__ == '__main__':
    s1 = "Hello"
    s2 = "World"
    gen = combined_generator(s1, s2)
    result = "".join(gen)
    print(result)