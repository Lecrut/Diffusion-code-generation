def combined_generator(s1: str, s2: str):
    i = j = 0
    while i < len(s1) or j < len(s2):
        if i < len(s1) and (j >= len(s2) or s1[i] <= s2[j]):
            yield s1[i]
            i += 1
        else:
            yield s2[j]
            j += 1
if __name__ == '__main__':
    result = list(combined_generator("abc", "def"))
    print(result)