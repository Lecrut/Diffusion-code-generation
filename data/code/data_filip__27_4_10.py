from functools import reduce

def rle_encode(s):
    if not s:
        return ''
    result = reduce(lambda acc, char: acc[:-2] + f"{acc[-2] if acc[-2:].isdigit() and int(acc[-2]) + 1 > 1 else ''}{char}" if acc and acc[-1] == char else acc + f"1{char}" if not acc or acc[-1] != char else acc, s, '')
    return ''.join([result[i:i+2] if result[i].isdigit() else f"1{result[i]}" for i in range(0, len(result), 2)]) if len(result) > 0 else result

if __name__ == '__main__':
    print(rle_encode('XYZXYZ'))