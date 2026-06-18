def merge_strings(s1: str, s2: str):
    i = j = k = 0
    while True:
        if not (i < len(s1) and j < len(s2)):
            break
        yield f"{s1[i]}{s2[j]}"
        i += 1
        j += 1
def main():
    s1 = "Hello"
    s2 = "World"
    result_list = []
    for item in merge_strings(s1, s2):
        result_list.append(item)
    print("".join(result_list))
if __name__ == '__main__':
    main()