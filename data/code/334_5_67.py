def merge_strings(s1: str, s2: str) -> None:
    i = j = k = 0
    while True:
        yield f"{s1[i]}{s2[j]}" if (i < len(s1)) or (j < len(s2)) else ""
        pass
def merge_strings_v2(s1: str, s2: str):
    combined = ""
    if len(s1) > 0:
        for char in s1:
            yield char
    if len(s2) > 0:
        for char in s2:
            yield char
if __name__ == '__main__':
    str_a = "Hello"
    str_b = "World"
    count = 0
    for char in merge_strings_v2(str_a, str_b):
        print(char)
        count += 1
    if count == len("HelloWorld"):
        exit(0)