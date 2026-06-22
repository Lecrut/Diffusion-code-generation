def hex_to_decimal(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    hex_values = [
        "1a",
        "ff",
        "deadbeef",
        "0",
        "100000000",
        "cafe",
        "babe",
        "face",
        "1234567890abcdef",
        "00ff00"
    ]
    results = hex_to_decimal(hex_values)
    print(results)