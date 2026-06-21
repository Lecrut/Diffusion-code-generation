def hex_batch_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    samples = ["FF", "1A", "deadbeef", "CAFE", "00", "ABCDEF"]
    results = hex_batch_to_decimal(samples)
    print(results)