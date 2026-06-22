def compress_run_length(data: bytes) -> bytes:
    if not data:
        return b""

    result = bytearray()
    length = len(data)
    i = 0

    while i < length:
        current_byte = data[i]
        run_length = 1
        while i + run_length < length and data[i + run_length] == current_byte and run_length < 255:
            run_length += 1
        result.append(run_length)
        result.append(current_byte)
        i += run_length

    return bytes(result)

if __name__ == "__main__":
    sample_data = b"AAAAAAAAAABBBCCCCCCDDDDD"
    compressed = compress_run_length(sample_data)
    print(compressed)
    sample_data2 = b""
    compressed2 = compress_run_length(sample_data2)
    print(compressed2)
    sample_data3 = b"X"
    compressed3 = compress_run_length(sample_data3)
    print(compressed3)