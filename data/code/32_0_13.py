def binary_to_hex(binary_str):
    if not binary_str:
        return "0"
    
    binary_str = binary_str.lstrip("0")
    if not binary_str:
        return "0"
    
    if not all(c in "01" for c in binary_str):
        raise ValueError("Invalid binary string")
    
    hex_digits = "0123456789abcdef"
    
    padded_len = len(binary_str) + (4 - len(binary_str) % 4) % 4
    padded = binary_str.zfill(padded_len)
    
    result = []
    for i in range(0, len(padded), 4):
        nibble = padded[i:i+4]
        val = 0
        for j, bit in enumerate(reversed(nibble)):
            if bit == "1":
                val += 2 ** j
        result.append(hex_digits[val])
    
    hex_str = "".join(result)
    hex_str = hex_str.lstrip("0")
    
    return hex_str if hex_str else "0"

if __name__ == "__main__":
    print(binary_to_hex("110101101111"))