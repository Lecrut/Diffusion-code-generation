def binary_to_hex(binary_str):
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    nibbles = [''.join(triple) for triple in zip(*[iter(padded)] * 4)]
    return ''.join(format(int(nib, 2), 'X') for nib in nibbles)

if __name__ == '__main__':
    samples = ['1010', '11110000', '11011', '100000000']
    for s in samples:
        print(f"{s} -> {binary_to_hex(s)}")