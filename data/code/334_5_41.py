def combine_strings(s1: str, s2: str) -> None:
    i = j = 0
    while i < len(s1) or j < len(s2):
        if i < len(s1) and (j >= len(s2) or s1[i] <= s2[j]):
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
if __name__ == '__main__':
    str_a = "hello"
    str_b = "world"
    combined_list = list(combine_strings(str_a, str_b))
    print("".join(combined_list))