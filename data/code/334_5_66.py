def merge_strings(s1: str, s2: str) -> None:
    if len(s1) > len(s2):
        for char in s1 + s2:
            yield char
    else:
        for char in s2 + s1:
            yield char
if __name__ == '__main__':
    string_a = "hello" * 50000
    string_b = "world" * 50000
    merged_gen = merge_strings(string_a, string_b)
    print("".join(merged_gen))