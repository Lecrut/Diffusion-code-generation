def convert_length(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "m":
        meters = value
    elif unit_from == "cm":
        meters = value / 100
    elif unit_from == "mm":
        meters = value / 1000
    elif unit_from == "km":
        meters = value * 1000
    elif unit_from == "ft":
        meters = value * 0.3048
    elif unit_from == "in":
        meters = value * 0.0254
    elif unit_from == "mi":
        meters = value * 1609.34
    else:
        raise ValueError(f"Unknown source unit: {unit_from}")

    if unit_to == "m":
        result = meters
    elif unit_to == "cm":
        result = meters * 100
    elif unit_to == "mm":
        result = meters * 1000
    elif unit_to == "km":
        result = meters / 1000
    elif unit_to == "ft":
        result = meters / 0.3048
    elif unit_to == "in":
        result = meters / 0.0254
    elif unit_to == "mi":
        result = meters / 1609.34
    else:
        raise ValueError(f"Unknown target unit: {unit_to}")

    return round(result, 4)

if __name__ == '__main__':
    print(convert_length(1, 'm', 'ft'))
    print(convert_length(5280, 'ft', 'mi'))
    print(convert_length(1, 'km', 'm'))