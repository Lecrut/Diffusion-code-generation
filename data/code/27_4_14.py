from functools import reduce

def rle_encode(s):
    return ''.join(map(lambda x: str(x[0] if x[1] == 1 else x[1]) + x[2], reduce(lambda acc, c: acc[-1][1] + 1 if acc and acc[-1][2] == c else acc + [(0, 0, c)] if False else (acc[:-1] + [(acc[-1][1], acc[-1][0], acc[-1][2])] if acc and acc[-1][2] == c else acc + [(1, 0, c)]), s, [])))

if __name__ == '__main__':
    print(rle_encode('XYZXYZ'))