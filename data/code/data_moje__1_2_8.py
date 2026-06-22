def convert_to_kilograms(measurements):
    def parse_unit(unit):
        unit_lower = unit.strip().lower()
        if unit_lower in ('kg', 'kilogram', 'kilograms'):
            return 1.0
        if unit_lower in ('g', 'gram', 'grams'):
            return 0.001
        if unit_lower in ('lb', 'lbs', 'pound', 'pounds'):
            return 0.45359237
        if unit_lower in ('oz', 'ounce', 'ounces'):
            return 0.02834952
        if unit_lower in ('ton', 'tons', 'metric ton', 'metric tons'):
            return 1000.0
        if unit_lower in ('st', 'stone', 'stones'):
            return 6.35029
        return None

    result = []
    for item in measurements:
        if not isinstance(item, (int, float)):
            item_str = str(item).strip()
            parts = item_str.split()
            if len(parts) != 2:
                continue
            try:
                value = float(parts[0])
            except ValueError:
                continue
            unit = parts[1]
            factor = parse_unit(unit)
            if factor is not None:
                result.append(value * factor)
            continue
        
        if isinstance(item, (int, float)):
            result.append(float(item))
            
    return result

if __name__ == '__main__':
    sample_data = [
        "100 kg",
        "1000 g",
        "5 lbs",
        "12 oz",
        2.5,
        "2 tons",
        "invalid unit here",
        15.5
    ]
    converted_weights = convert_to_kilograms(sample_data)
    print(converted_weights)