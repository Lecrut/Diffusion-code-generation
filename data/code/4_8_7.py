import math
def normalize_distance(distance, original_unit):
    if original_unit == "meter":
        return distance
    elif original_unit == "kilometer":
        return distance * 1000.0
    elif original_unit == "centimeter":
        return distance / 100.0
    elif original_unit == "millimeter":
        return distance / 1000.0
    else:
        raise ValueError("Unsupported unit")
if __name__ == '__main__':
    distances = [
        (10.0, "meter"),
        (2.5, "kilometer"),
        (500.0, "centimeter"),
        (1234.56, "millimeter"),
        (0.003, "kilometer")
    ]
    print("--- Distance Normalization ---")
    for distance, unit in distances:
        try:
            normalized = normalize_distance(distance, unit)
            print(f"Original: {distance} {unit} -> Normalized: {normalized} meters")
        except ValueError as e:
            print(f"Error processing {distance} {unit}: {e}")