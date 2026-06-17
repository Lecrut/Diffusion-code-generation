def combined_generator(s1: str, s2: str):
    i = j = 0
    while True:
        if i < len(s1) and (j >= len(s2)):
            yield s1[i]
            i += 1
        elif j < len(s2) and (i >= len(s1)):
            yield s2[j]
            j += 1
        else:
            break
if __name__ == '__main__':
    str_a = "hello"
    str_b = "world"
    gen_obj = combined_generator(str_a, str_b)
    result_list = []
    for char in gen_obj:
        result_list.append(char)
    print("".join(result_list))