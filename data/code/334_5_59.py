def combined_generator(s1: str, s2: str):
    i = j = 0
    while i < len(s1) or j < len(s2):
        if i < len(s1):
            yield s1[i]
            i += 1
        elif j < len(s2):
            yield s2[j]
            j += 1
if __name__ == '__main__':
    str_a = "Hello"
    str_b = "World"
    result_list = list(combined_generator(str_a, str_b))
    print("".join(result_list))