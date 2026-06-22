def normalize_to_meters(distance, unit):
    if unit == "m":
        return distance
    elif unit == "km":
        return distance * 1000
    elif unit == "cm":
        return distance / 100
    elif unit == "mm":
        return distance / 1000
    elif unit == "mi":
        return distance * 1609.344
    elif unit == "yd":
        return distance * 0.9144
    elif unit == "ft":
        return distance * 0.3048
    elif unit == "in":
        return distance * 0.0254
    elif unit == "nm":
        return distance * 1852
    else:
        raise ValueError(f"Unknown unit: {unit}")

if __name__ == '__main__':
    print(normalize_to_meters(1, "km"))
    print(normalize_to_meters(1, "mi"))
    print(normalize_to_meters(100, "cm"))
    print(normalize_to_meters(1, "nm"))
    print(normalize_to_meters(60, "in"))