def merge_strings(str1: str, str2: str) -> None:
    for i in range(max(len(str1), len(str2))):
        if i < len(str1):
            yield str1[i]
        if i < len(str2):
            yield str2[i]
if __name__ == '__main__':
    s_a = "Hello" * 10**6
    s_b = "World" * 10**6
    gen = merge_strings(s_a, s_b)
    for _ in range(5):
        print(next(gen), end="")