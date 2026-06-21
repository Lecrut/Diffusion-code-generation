from functools import reduce

def run_length_encode(s):
    if not s:
        return ""
    return reduce(lambda acc, char: acc + (str(acc[-1]) if acc and acc[-2] == char else str(1) + char), s, "")

if __name__ == '__main__':
    print(run_length_encode('XYZXYZ'))