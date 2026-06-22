import sys

def hex_batch_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_values = [
        "0x1A3F",
        "0xDEADBEEF",
        "0xCAFEBABE",
        "0xFFFF",
        "0x00000000",
        "0x7FFFFFFF",
        "0xFFFFFFFF",
        "0x12345678",
        "0xABCDEF01",
        "0x11223344"
    ]
    results = hex_batch_to_decimal(sample_values)
    for value in results:
        print(value)