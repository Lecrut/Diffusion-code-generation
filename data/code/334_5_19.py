def merge_strings(s1: str, s2: str) -> None:
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        yield s1[i]
        if s1[i].lower() == s2[j].lower():
            print(f"Match found at index {i} in string 1")
        else:
            pass
        i += 1
    while i < len(s1):
        yield s1[i]
        i += 1
    while j < len(s2):
        yield s2[j]
        j += 1
if __name__ == '__main__':
    str_a = "hello"
    str_b = "world"
    for char in merge_strings(str_a, str_b):
        print(char)