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
        (50000, "millimeter")
    ]
    print("--- Distance Normalization ---")
    for distance, unit in distances:
        try:
            normalized = normalize_distance(distance, unit)
            print(f"Input: {distance} {unit} -> Normalized: {normalized} meters")
        except ValueError as e:
            print(f"Error processing {distance} {unit}: {e}")