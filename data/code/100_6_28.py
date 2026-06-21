def validate_and_sequence(bits):
    if not bits or len(bits) < 2:
        raise ValueError("Invalid sequence")
    for b in bits:
        if b not in ('0', '1'):
            raise ValueError("Invalid character")
    input_bits = bits[:-1]
    result_bit = bits[-1]
    computed = '1' if all(b == '1' for b in input_bits) else '0'
    return result_bit == computed

if __name__ == '__main__':
    seq = "1111"
    print(validate_and_sequence(seq))