def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    hex_values = ["ff", "10", "0", "dead"]
    for h in hex_values:
        print(hex_to_decimal(h))