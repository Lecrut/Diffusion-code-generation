def run_length_encode(s):
    if not s:
        return s
    return ''.join(
        f"{count}{char}" if count > 1 else char
        for char, group in __import__('itertools').groupby(s)
        for count in [len(list(group))]
    )

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("abc"))