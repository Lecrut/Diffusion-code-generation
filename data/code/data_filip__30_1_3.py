def to_twos_complement(n, bits=8):
    mask = (1 << bits) - 1
    if n < 0:
        val = (1 << bits) + n
    else:
        val = n
    if val < 0 or val > mask:
        raise ValueError(f"Value {n} out of range for {bits} bits")
    binary = bin(val & mask)[2:].zfill(bits)
    return binary

def main():
    print(to_twos_complement(-1, 8))
    print(to_twos_complement(5, 8))
    print(to_twos_complement(-128, 8))

if __name__ == '__main__':
    main()