def combined_generator(str1: str, str2: str):
    for char in (str1 + str2):
        yield char
if __name__ == '__main__':
    s_a = "Hello"
    s_b = "World"
    gen = combined_generator(s_a, s_b)
    result_list = list(gen)
    print("".join(result_list))