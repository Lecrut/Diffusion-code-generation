def hex_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex = ["FF", "1A2B", "0", "10", "ABCDEF"]
    results = hex_to_decimal(sample_hex)
    print(results)