def yield_combined(s1: str, s2: str):
    i = j = k = 0
    while True:
        if i < len(s1) and (j >= len(s2) or ord(s1[i]) <= ord(s2[j])):
            yield s1[i]
            i += 1
        elif j < len(s2):
            yield s2[j]
            j += 1
        else:
            break
if __name__ == '__main__':
    str_a = "hello"
    str_b = "world"
    result = "".join(yield_combined(str_a, str_b))
    print(result)