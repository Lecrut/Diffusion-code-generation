def compress_rle(binary_sequence: list[int]) -> str:
    if not binary_sequence:
        return ""

    result = []
    count = 0
    current_bit = binary_sequence[0]

    for bit in binary_sequence:
        if bit == current_bit:
            count += 1
        else:
            result.append(f"{count}{current_bit}")
            current_bit = bit
            count = 1

    result.append(f"{count}{current_bit}")
    return "".join(result)

if __name__ == '__main__':
    sample = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    compressed = compress_rle(sample)
    print(compressed)