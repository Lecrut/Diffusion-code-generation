def binary_to_hex(binary_str):
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    groups = [''.join(group) for group in zip(*[iter(padded)] * 4)]
    return ''.join([hex(int(g, 2))[2:].upper() for g in groups])

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('111100001111'))
    print(binary_to_hex('1'))