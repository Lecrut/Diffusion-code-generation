def run_length_encode(s):
    if not s:
        return ""
    return "".join(
        str(len(list(group))) + char
        for char, group in ((c, g) for c, g in __import__("itertools").groupby(s))
    )

if __name__ == "__main__":
    print(run_length_encode("AABBBCC"))
    print(run_length_encode("ABC"))
    print(run_length_encode(""))
    print(run_length_encode("AAAA"))