import sys

def hex_batch_to_dec(hex_list):
    return [int(h, 16) for h in hex_list]

if __name__ == '__main__':
    sample_hex_values = ["0x1A", "0xFF", "0x4B", "0xDEADBEEF", "0x123456789ABCDEF0"]
    results = hex_batch_to_dec(sample_hex_values)
    for val in results:
        print(val)