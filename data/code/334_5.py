def merge_strings(s1: str, s2: str):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
if __name__ == '__main__':
    str_a = "abc"
    str_b = "def"
    merged_iter = merge_strings(str_a, str_b)
    result_list = list(merged_iter)
    print("".join(result_list))