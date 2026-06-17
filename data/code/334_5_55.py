def merge_strings(s1: str, s2: str):
    i = j = k = 0
    while i < len(s1) and j < len(s2):
        if ord(s1[i]) <= ord(s2[j]):
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
    while i < len(s1):
        yield s1[i]
        i += 1
    while j < len(s2):
        yield s2[j]
        j += 1
if __name__ == '__main__':
    str_a = "apple"
    str_b = "banana"
    merged_result = "".join(merge_strings(str_a, str_b))
    print(f"Merged: {merged_result}")