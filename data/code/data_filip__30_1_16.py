def to_twos_complement_binary(number):
    if number >= 0:
        return bin(number)[2:]
    mask = (1 << 32) - 1
    return bin(number & mask)[2:]

def main():
    sample_values = [5, -5, 0, -1, 127, -128]
    for val in sample_values:
        print(to_twos_complement_binary(val))

if __name__ == '__main__':
    main()