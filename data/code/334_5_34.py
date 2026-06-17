def combined_generator(s1: str, s2: str):
    i = j = k = 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
    while i < len(s1):
        yield s1[i]
        i += 1
    while j < len(s2):
        yield s2[j]
        j += 1
if __name__ == '__main__':
    str_a = "banana"
    str_b = "apple"
    result_list = list(combined_generator(str_a, str_b))
    print("".join(result_list))