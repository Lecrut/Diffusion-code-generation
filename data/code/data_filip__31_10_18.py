def hex_to_decimal(hex_string):
    if not hex_string:
        return 0
    cleaned = hex_string.strip()
    if cleaned.startswith('-'):
        sign = -1
        cleaned = cleaned[1:]
    else:
        sign = 1
    result = int(cleaned, 16)
    return sign * result

if __name__ == '__main__':
    samples = ["0A", "1F", "FF", "0", "-1A"]
    for sample in samples:
        print(hex_to_decimal(sample))