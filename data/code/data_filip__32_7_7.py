def binary_to_hex(binary_str):
    return ''.join(hex(int(''.join(chunk), 2))[2:].upper().zfill(1) if int(''.join(chunk), 2) > 0 else '0' for chunk in zip(*[iter(binary_str.zfill((len(binary_str) + 3) // 4 * 4))]*4))

if __name__ == '__main__':
    sample_binaries = ['1010', '11110000', '101010101010', '1']
    results = [binary_to_hex(b) for b in sample_binaries]
    print(results)