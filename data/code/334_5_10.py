def merge_strings(s1: str, s2: str) -> None:
    i = j = k = 0
    while True:
        if i < len(s1):
            yield s1[i]
            i += 1
        elif j < len(s2):
            yield s2[j]
            j += 1
        else:
            break
if __name__ == '__main__':
    str_a = "Hello"
    str_b = "World!"
    result_list = []
    for char in merge_strings(str_a, str_b):
        result_list.append(char)
    print("".join(result_list))