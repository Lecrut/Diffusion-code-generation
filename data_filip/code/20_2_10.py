def compress_rle(sequence: bytes) -> list:
    if not sequence:
        return []

    compressed = []
    current_byte = sequence[0]
    run_length = 1

    for byte in sequence[1:]:
        if byte == current_byte and run_length < 255:
            run_length += 1
        else:
            compressed.append((current_byte, run_length))
            current_byte = byte
            run_length = 1

    compressed.append((current_byte, run_length))
    return compressed

if __name__ == '__main__':
    sample_data = b'AAABBBCCCDDDDD'
    result = compress_rle(sample_data)
    print(result)