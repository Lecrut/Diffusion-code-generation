def to_twos_complement(n: int, bits: int = 32) -> str:
    if n >= 0:
        binary = bin(n)[2:].zfill(bits)
        if len(binary) > bits:
            raise ValueError(f"Number {n} cannot be represented in {bits} bits.")
        return binary
    
    if n < -(2 ** (bits - 1)):
        raise ValueError(f"Number {n} is out of range for {bits}-bit signed integers.")
    
    mask = (1 << bits) - 1
    twos_complement = n & mask
    binary = bin(twos_complement)[2:].zfill(bits)
    return binary

def main():
    print(to_twos_complement(5))
    print(to_twos_complement(-5))
    print(to_twos_complement(0))
    print(to_twos_complement(-128, 8))
    print(to_twos_complement(127, 8))

if __name__ == '__main__':
    main()