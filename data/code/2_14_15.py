def convert_volumes_to_milliliters(volumes):
    conversion_factors = {
        "liter": 1000.0,
        "gallon": 3785.411784,
        "cubic_inch": 16.387064
    }
    result = []
    for item in volumes:
        value = item["value"]
        unit = item["unit"].lower().replace(" ", "_")
        if value < 0:
            raise ValueError("Negative volume not allowed")
        if value == 0:
            result.append(0.0)
            continue
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {item['unit']}")
        ml_value = value * conversion_factors[unit]
        result.append(ml_value)
    return result

if __name__ == '__main__':
    sample_data = [
        {"value": 1, "unit": "liter"},
        {"value": 2, "unit": "gallon"},
        {"value": 500, "unit": "cubic inches"},
        {"value": 0, "unit": "liter"}
    ]
    converted = convert_volumes_to_milliliters(sample_data)
    print(converted)