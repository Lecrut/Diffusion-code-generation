from functools import reduce
def rle_encode(s):
    if not s:
        return ""
    return reduce(lambda acc, ch: acc[:-1] + str(acc[-1][1] + 1) if acc and acc[-1][0] == ch else acc + [(ch, 1)], s, [('', 0)])[1:]
if __name__ == '__main__':
    print(rle_encode('XYZXYZ'))