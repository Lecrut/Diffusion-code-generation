def twos_complement_binary(number):
    if number >= 0:
        return bin(number)[2:]
    bit_length = len(bin(number & 0xFFFFFFFF)[2:])
    mask = (1 << bit_length) - 1
    complement = number & mask
    return bin(complement)[2:]

if __name__ == '__main__':
    sample_values = [-1, -5, -10, 0, 5, 10, -2**8, 2**8]
    for value in sample_values:
        result = twos_complement_binary(value)
        print(f"twos_complement_binary({value}) -> '{result}'")