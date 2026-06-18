def merge_generator(s1: str, s2: str):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
    remaining = s1[i:] or s2[j:]
    for char in remaining:
        yield char
if __name__ == '__main__':
    str_a = "banana"
    str_b = "apple"
    result_list = []
    for item in merge_generator(str_a, str_b):
        result_list.append(item)
    print("".join(result_list))