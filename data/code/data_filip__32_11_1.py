import re

def binary_to_hex_upper(binary_strings):
    if not isinstance(binary_strings, list):
        raise TypeError("Input must be a list of strings")
    results = []
    for bs in binary_strings:
        if not isinstance(bs, str):
            raise TypeError("Each element must be a string")
        if not re.match(r'^[01]+$', bs):
            raise ValueError(f"Invalid binary string: {bs}")
        decimal_val = int(bs, 2)
        hex_val = hex(decimal_val)[2:].upper()
        results.append(hex_val)
    return results

if __name__ == '__main__':
    sample_inputs = ["1010", "1100", "1111", "1000", "1101"]
    result = binary_to_hex_upper(sample_inputs)
    print(result)