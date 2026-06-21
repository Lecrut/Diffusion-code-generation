from functools import reduce

def rle_encode(s):
    return reduce(lambda acc, c: acc[:-2] + str(int(acc[-2]) + 1) + acc[-1] if acc and acc[-1] == c else (acc + '1' + c if acc else '1' + c), s, '')

if __name__ == '__main__':
    print(rle_encode('XYZXYZ'))