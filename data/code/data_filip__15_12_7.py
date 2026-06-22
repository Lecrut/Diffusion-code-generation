import itertools

def compress_sequence(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == "__main__":
    test_string = "aaabbccccd"
    print(compress_sequence(test_string))