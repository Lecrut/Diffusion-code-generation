HEX_COLOR_CONSTANTS = {
    "FF0000": 16711680,
    "00FF00": 65280,
    "0000FF": 255,
    "FFFF00": 16776960,
    "00FFFF": 65535,
    "FF00FF": 16711935,
    "FFFFFF": 16777215,
    "000000": 0,
    "808080": 8421504,
    "C0C0C0": 12632256
}

def normalize_hex_input(raw_hex):
    stripped = raw_hex.strip()
    if stripped.startswith("#"):
        stripped = stripped[1:]
    return stripped.upper()

def convert_hex_to_decimal_value(hex_string):
    normalized = normalize_hex_input(hex_string)
    if normalized in HEX_COLOR_CONSTANTS:
        return HEX_COLOR_CONSTANTS[normalized]
    if len(normalized) == 6:
        return int(normalized, 16)
    if len(normalized) == 3:
        expanded = normalized[0]*2 + normalized[1]*2 + normalized[2]*2
        return int(expanded, 16)
    return -1

def map_sample_colors():
    sample_inputs = ["#FF0000", "#00FF00", "#0000FF", "#fff", "#000"]
    results = {}
    for h in sample_inputs:
        decimal_val = convert_hex_to_decimal_value(h)
        results[h] = decimal_val
    return results

if __name__ == '__main__':
    output_data = map_sample_colors()
    print(output_data)