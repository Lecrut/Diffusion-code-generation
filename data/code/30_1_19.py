def two_complement_binary(n):
    if n >= 0:
        return bin(n)[2:]
    else:
        return bin(n & 0xFFFFFFFF)[2:]

if __name__ == '__main__':
    sample_values = [5, -5, 0, -1, 127, -128]
    for value in sample_values:
        result = two_complement_binary(value)
        print(f"{value}: {result}")