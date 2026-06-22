def binary_to_hex(binary_strings):
    results = []
    for s in binary_strings:
        if not s:
            raise ValueError("Empty string provided")
        for char in s:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid binary character '{char}' in string '{s}'")
        results.append(hex(int(s, 2))[2:].upper())
    return results

if __name__ == '__main__':
    samples = [
        "1010",
        "1111",
        "10000",
        "10101010",
        "11111111"
    ]
    result = binary_to_hex(samples)
    print(result)