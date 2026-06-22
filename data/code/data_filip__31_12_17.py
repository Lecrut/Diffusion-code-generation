import time

def convert_hex_batch(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_data = ["0x1A", "0xFF", "0x1000", "0xDEADBEEF", "0x0", "0xCAFE"]
    start_time = time.perf_counter()
    result = convert_hex_batch(sample_data)
    end_time = time.perf_counter()
    print(result)
    print(f"Time taken: {(end_time - start_time) * 1000:.4f} ms")