def convert_volume_strings(volumes):
    mapping = {
        "ml": 1e-6,
        "l": 0.001,
        "m3": 1.0,
        "cm3": 1e-6,
        "dL": 0.01,
        "cL": 0.001,
    }
    def parse_volume(value):
        try:
            num = float(value)
        except ValueError:
            return None
        unit_str = value.split()[-1].lower().rstrip("ml") if "." in str(num).split()[0] else ""
        for key, factor in mapping.items():
            if key == "m3":
                continue
            suffixes = [key + "l", key]
            for s in suffixes:
                if value.endswith(s):
                    return num * factor
    result = []
    for item in volumes:
        parsed = parse_volume(item)
        if isinstance(parsed, float):
            result.append(parsed)
    return result
if __name__ == '__main__':
    sample_data = [
        "50ml", 
        "2.5l", 
        "1m3", 
        "invalid", 
        "75cm3"
    ]
    converted_values = convert_volume_strings(sample_data)
    print(converted_values)