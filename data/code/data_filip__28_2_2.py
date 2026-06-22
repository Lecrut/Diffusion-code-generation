def compress_string(s):
    if not s:
        return ""
    return "".join(f"{count}{char}" for char, group in __import__("itertools").groupby(s) for count in [sum(1 for _ in group)] for char in [char] if count > 0)

if __name__ == '__main__':
    sample = "AAAAAABBBCCCCDDDDDDDDDDDEEEFFFFFGGGGGHHHHHHIIIIIIIIIIJJJJJJJJJJJJJJJJJJJ"
    result = compress_string(sample)
    print(result)