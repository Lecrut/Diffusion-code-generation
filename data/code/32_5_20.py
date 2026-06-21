def binary_to_hex_chunked(binary_str: str, chunk_size: int = 8192) -> str:
    if not binary_str:
        return ""
    if len(binary_str) % 4 != 0:
        padded_len = len(binary_str) + (4 - len(binary_str) % 4)
        binary_str = "0" * (padded_len - len(binary_str)) + binary_str
    result = []
    for i in range(0, len(binary_str), chunk_size):
        chunk = binary_str[i : i + chunk_size]
        result.append(hex(int(chunk, 2))[2:])
    return "".join(result)

if __name__ == "__main__":
    sample_binary = "1101101111001000111011100011100101010000011111110000111100000001" * 1000
    hex_result = binary_to_hex_chunked(sample_binary)
    print(hex_result)