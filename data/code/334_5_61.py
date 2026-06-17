def merge_strings(s1: str, s2: str) -> None:
    i = j = 0
    while i < len(s1) and j < len(s2):
        yield s1[i]
        if s1[i] == s2[j]:
            yield s2[j]
        i += 1
        j += 1
def main() -> None:
    str_a = "Hello"
    str_b = "World"
    for char in merge_strings(str_a, str_b):
        print(char)
if __name__ == '__main__':
    main()