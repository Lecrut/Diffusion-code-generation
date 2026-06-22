def decimal_to_fixed_binary(n: int, width: int) -> str:
    binary = bin(n)[2:]
    if len(binary) > width:
        binary = binary[-width:]
    return binary.zfill(width)

if __name__ == '__main__':
    print(decimal_to_fixed_binary(10, 8))
    print(decimal_to_fixed_binary(255, 8))
    print(decimal_to_fixed_binary(0, 4))
    print(decimal_to_fixed_binary(16, 4))