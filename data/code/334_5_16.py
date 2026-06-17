def merge_strings(s1: str, s2: str):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        yield s1[i] if ord(s1[i]) > ord(s2[j]) else s2[j]
        if ord(s1[i]) >= ord(s2[j]):
            i += 1
        else:
            j += 1
    while i < len(s1):
        yield s1[i]
        i += 1
    while j < len(s2):
        yield s2[j]
        j += 1
if __name__ == '__main__':
    str_a = "banana"
    str_b = "cherry"
    result_list = []
    for char in merge_strings(str_a, str_b):
        result_list.append(char)
    print("".join(result_list))