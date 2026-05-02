import math
def normalize_distance(distance, unit):
    if unit == "m":
        return distance
    elif unit == "km":
        return distance * 1000.0
    elif unit == "cm":
        return distance / 100.0
    elif unit == "mm":
        return distance / 1000.0
    else:
        raise ValueError("Unsupported unit")
if __name__ == '__main__':
    distances_to_normalize = [
        (10.0, "m"),
        (2.5, "km"),
        (500.0, "cm"),
        (1500.0, "mm"),
        (3.14159, "m")
    ]
    results = []
    for dist, unit in distances_to_normalize:
        try:
            normalized_value = normalize_distance(dist, unit)
            results.append((dist, unit, normalized_value))
        except ValueError as e:
            results.append((dist, unit, f"Error: {e}"))
    for dist, unit, norm in results:
        print(f"Original: {dist} {unit} -> Normalized (meters): {norm}")