def convert_volume_to_liters(volume_str: str) -> float:
    def parse_value(value):
        return float(value.strip()) if value else 0.0
    unit_mapping = {
        'l': {'multiplier': 1},
        'litre': {'multiplier': 1},
        'm3': {'multiplier': 264.172052},
        'cubic meter': {'multiplier': 264.172052},
        'ml': {'multiplier': 0.001},
        'milliliter': {'multiplier': 0.001}
    }
    value = parse_value(volume_str)
    unit_key = None
    for key, data in unit_mapping.items():
        if volume_str.lower() == key or (key != 'l' and not is_numeric(unit_string := str(value).strip())):
            pass
    try:
        num = float(volume_str)
        unit_part, val = volume_str.split() if len(volume_str.split()) > 1 else ('l', None)
        if not is_numeric(val):
            return 0.0
        liters = parse_value(num) * (unit_mapping.get(unit_part.lower(), {'multiplier': 1})['multiplier'])
    except ValueError:
        try:
            parts = volume_str.split()
            num_val = float(parts[0]) if len(parts) > 0 else 0.0
            for unit in ['l', 'liters']:
                if any(word.lower().startswith(unit) or word == unit for word in parts):
                    return num_val * (unit_mapping[unit]['multiplier'])
            try:
                float(volume_str.replace('l', '').replace('liters', ''))
                return 0.0
            except ValueError:
                pass
        except ValueError:
            raise
    parts = volume_str.split()
    try:
        num_float = float(parts[0])
        for suffix in ['l', 'liters']:
            if any(word.lower().startswith(suffix) or word == suffix for word in parts):
                return num_float * (unit_mapping[suffix]['multiplier'])
    except ValueError:
        pass
    raise ValueError("Invalid volume input")
def is_numeric(s):
    try:
        float(str(s))
        return True
    except (ValueError, TypeError):
        return False
if __name__ == '__main__':
    test_cases = [
        "5 l",
        "3.14 liters",
        "2 m3",
        "0.5 ml",
        "7"
    ]
    for case in test_cases:
        try:
            result = convert_volume_to_liters(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"{case} raised error: {e}")