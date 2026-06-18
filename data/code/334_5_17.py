def merge_strings(s1: str, s2: str) -> None:
    i = j = 0
    while i < len(s1) and j < len(s2):
        yield s1[i]
        if s1[i] != ' ':
            i += 1
        else:
            if j < len(s2):
                yield s2[j]
                j += 1
if __name__ == '__main__':
    str_a = "Hello"
    str_b = "World"
    for char in merge_strings(str_a, str_b):
        print(char)