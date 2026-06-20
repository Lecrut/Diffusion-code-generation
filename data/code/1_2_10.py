def convert_to_kilograms(measurements):
    conversions = {
        'g': 0.001,
        'kg': 1.0,
        'lb': 0.453592,
        'oz': 0.0283495,
        'mg': 0.000001
    }
    results = []
    for item in measurements:
        if isinstance(item, (int, float)):
            results.append(float(item))
        elif isinstance(item, str):
            parts = item.strip().lower().split()
            if len(parts) == 2:
                try:
                    value = float(parts[0])
                    unit = parts[1]
                    if unit in conversions:
                        results.append(value * conversions[unit])
                    else:
                        results.append(None)
                except ValueError:
                    results.append(None)
            else:
                results.append(None)
        else:
            results.append(None)
    return results

if __name__ == '__main__':
    data = [100.0, "200 g", "5 lb", "10 oz", "3.5 kg", "bad input", "400 mg"]
    output = convert_to_kilograms(data)
    print(output)