def combined_generator(s1: str, s2: str):
    i = j = k = 0
    while True:
        if i < len(s1) and (j >= len(s2) or s1[i] <= s2[j]):
            yield s1[i]
            i += 1
        elif j < len(s2) and (i >= len(s1) or s2[j] < s1[i]):
            yield s2[j]
            j += 1
        else:
            break
if __name__ == '__main__':
    str_a = "banana"
    str_b = "apple"
    result_list = list(combined_generator(str_a, str_b))
    print("".join(result_list))