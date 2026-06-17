def convert_volumes(volume_strings):
    mapping = {
        "L": 1000,
        "m³": 1000,
        "gal": 3.78541,
        "qt": 0.946353,
        "pt": 0.473176,
    }
    def parse_volume(s):
        s = str(s).strip().lower()
        if not any(k in s for k in mapping.keys()):
            raise ValueError(f"Unsupported unit: {s}")
        value_str = ""
        multiplier = 0.0
        for i, char in enumerate(s):
            if char.isdigit():
                value_str += char
            elif char == " ":
                continue
            else:
                break
        try:
            val = float(value_str)
        except ValueError:
            raise ValueError(f"Invalid number format: {s}")
        unit_part = s[i:] if i < len(s) and not value_str.isdigit() or (i == 0 and any(c in mapping for c in s)) else ""
        parts = []
        num_found = False
        idx_start = -1
        end_idx = len(s)
        if "gal" in s:
            multiplier = 3.78541
            for i, c in enumerate(s):
                if not num_found and (c.isdigit() or c == "."):
                    parts.append(c)
                    idx_start = end_idx - len(parts) + 1                                                    
        return val * multiplier
    def clean_and_convert(item):
        item_str = str(item).strip().lower()
        if not any(k in item_str for k in ["l", "m³", "gal", "qt", "pt"]):
            raise ValueError(f"Unknown volume unit: {item}")
        num_part, unit_part = "", ""
        i = 0
        while i < len(item_str) and (item_str[i].isdigit() or item_str[i] == "."):
            num_part += item_str[i]
            i += 1
        if i >= len(item_str):
             raise ValueError(f"Missing unit in: {item}")
        j = len(item_str) - 1
        while j > 0 and item_str[j].isdigit():
            j -= 1
        if j == 0 or not any(c in mapping for c in item_str):
             raise ValueError(f"Invalid format: {item}")
        unit_key = ""
        for k, v in mapping.items():
            if k.lower() in item_str[j:] and j + len(k) <= len(item_str):
                unit_key = k
        val = float(num_part) * (mapping[unit_key] / 1000.0 if "m³" not in item_str else 1.0)                                  
    return [clean_and_convert(x) for x in volume_strings]
if __name__ == '__main__':
    sample_data = ["5 L", "2 m³", "3 gal", "4 qt", "6 pt"]
    try:
        result = convert_volumes(sample_data)
        print(result)
    except Exception as e:
        print(f"Error: {e}")