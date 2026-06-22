import time

def hex_batch_to_int(hex_values):
    return [int(x, 16) for x in hex_values]

if __name__ == '__main__':
    sample_hex_data = [
        "0x1A", "0xFF", "0xDEADBEEF", "0xCAFEBABE",
        "0x00", "0x80", "0x1000", "0xFFFF",
        "0xABCDEF", "0x123456789ABCDEF"
    ]
    results = hex_batch_to_int(sample_hex_data)
    print(results)