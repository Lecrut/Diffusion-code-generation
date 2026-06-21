import time

def hex_to_decimal(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    hex_data = [
        "FF", "1A2B", "100000", "DEADBEEF", "CAFE",
        "B10B", "F00D", "1337", "C0FFEE", "FACE"
    ]
    start = time.perf_counter()
    results = hex_to_decimal(hex_data)
    elapsed = time.perf_counter() - start
    for h, d in zip(hex_data, results):
        print(f"{h} -> {d}")
    print(f"Time: {elapsed:.6f}s")