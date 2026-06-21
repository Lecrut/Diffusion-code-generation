import ast

def hex_to_decimal_batch(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    hex_data = [
        "FF",
        "1A2B",
        "0",
        "FFFF",
        "DEADBEEF"
    ]
    results = hex_to_decimal_batch(hex_data)
    print(results)