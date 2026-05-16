import math
def normalize_distance(distance, unit):
    if unit == "m":
        return distance
    elif unit == "km":
        return distance * 1000
    elif unit == "cm":
        return distance / 100
    elif unit == "mm":
        return distance / 1000
    else:
        raise ValueError("Unsupported unit")
if __name__ == '__main__':
    distances_to_normalize = [
        (5.5, "km"),
        (1200, "cm"),
        (3500, "mm"),
        (10.2, "m"),
        (1.5, "km")
    ]
    results = []
    for distance, unit in distances_to_normalize:
        try:
            normalized_value = normalize_distance(distance, unit)
            results.append((distance, unit, normalized_value))
        except ValueError as e:
            results.append((distance, unit, f"Error: {e}"))
    for dist, unit, norm in results:
        print(f"Original: {dist} {unit} -> Normalized (m): {norm}")