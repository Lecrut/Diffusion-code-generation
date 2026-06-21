def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string.")
    if not hex_string:
        raise ValueError("Input string cannot be empty.")
    valid_chars = set("0123456789abcdefABCDEF")
    if not set(hex_string).issubset(valid_chars):
        raise ValueError("Invalid hex characters detected.")
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError("Invalid hex string format.")

if __name__ == '__main__':
    results = []
    for val in ["1a", "FF", "0", "10", "GHI"]:
        try:
            res = hex_to_decimal(val)
            results.append((val, res))
        except ValueError as e:
            results.append((val, str(e)))
    for v, r in results:
        print(f"hex_to_decimal('{v}') = {r}")