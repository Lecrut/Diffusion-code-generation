def rle_encode(s):
    if not s:
        return ""
    return "".join(str(count) + char for char, count in [(char, len(list(grp))) for char, grp in __import__('itertools').groupby(s)])

if __name__ == '__main__':
    print(rle_encode("aaabbc"))
    print(rle_encode(""))
    print(rle_encode("a"))