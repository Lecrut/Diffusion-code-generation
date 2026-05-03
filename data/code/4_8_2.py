import math
def normalize_distance(distance, unit):
    if unit == "meter":
        return distance
    elif unit == "kilometer":
        return distance * 1000
    elif unit == "centimeter":
        return distance / 100
    elif unit == "millimeter":
        return distance / 1000
    else:
        raise ValueError("Unsupported unit")
if __name__ == '__main__':
    distances = [
        (500, "meter"),
        (2.5, "kilometer"),
        (150, "centimeter"),
        (3500, "millimeter")
    ]
    results = []
    for dist, unit in distances:
        try:
            normalized = normalize_distance(dist, unit)
            results.append((dist, unit, normalized))
        except ValueError as e:
            results.append((dist, unit, f"Error: {e}"))
    for dist, unit, normalized in results:
        print(f"Original: {dist} {unit}, Normalized (meters): {normalized}")