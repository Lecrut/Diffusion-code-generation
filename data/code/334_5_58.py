def combined_generator(s1: str, s2: str):
    i, j = 0, 0
    while i < len(s1) or j < len(s2):
        if i < len(s1) and (j >= len(s2) or ord(s1[i]) <= ord(s2[j])):
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
if __name__ == '__main__':
    str_a = "hello"
    str_b = "world"
    result_list = list(combined_generator(str_a, str_b))
    print("".join(result_list))