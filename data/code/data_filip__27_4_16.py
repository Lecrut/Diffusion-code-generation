from functools import reduce
def rle(s):
    if not s: return []
    def step(acc, c):
        if not acc: return [(c, 1)]
        last, cnt = acc[-1]
        if last == c: acc[-1] = (last, cnt + 1)
        else: acc.append((c, 1))
        return acc
    return reduce(step, s, [])
if __name__ == '__main__':
    print(rle('XYZXYZ'))