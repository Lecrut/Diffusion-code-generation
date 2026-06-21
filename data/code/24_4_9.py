def compress_rle(text):
    if not text:
        return ""
    groups = []
    for char, group in itertools.groupby(text):
        length = len(list(group))
        if length == 1:
            groups.append(char)
        else:
            groups.append(f"{length}{char}")
    return "".join(groups)

import itertools

if __name__ == '__main__':
    sample_text = "AAABBBCCCAAD"
    result = compress_rle(sample_text)
    print(result)