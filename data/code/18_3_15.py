from itertools import groupby

def run_length_encode(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = len(list(group))
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    encoded = run_length_encode(sample_string)
    print(encoded)