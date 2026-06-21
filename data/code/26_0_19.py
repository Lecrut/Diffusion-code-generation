import itertools

def run_length_encode(s):
    if not s:
        return []
    groups = itertools.groupby(s)
    encoded = []
    for key, group_iter in groups:
        count = sum(1 for _ in group_iter)
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    print(run_length_encode("AAABBBCCDAA"))
    print(run_length_encode("ABC"))
    print(run_length_encode(""))
    print(run_length_encode("AAAA"))