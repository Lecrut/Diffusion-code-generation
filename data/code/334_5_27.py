def merge_strings(s1: str, s2: str) -> None:
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            yield s1[i]
        if i < len(s2):
            yield s2[i]
if __name__ == '__main__':
    str_a = "Hello"
    str_b = "World"
    result_list = []
    for char in merge_strings(str_a, str_b):
        result_list.append(char)
    print("".join(result_list))