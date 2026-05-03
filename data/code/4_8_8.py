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
    distances = [
        (10.5, "m"),
        (2.5, "km"),
        (500.0, "cm"),
        (1234.56, "mm"),
        (3.14159, "m")
    ]
    print("--- Distance Normalization ---")
    for distance, unit in distances:
        try:
            normalized = normalize_distance(distance, unit)
            print(f"Input: {distance} {unit} -> Normalized: {normalized} m")
        except ValueError as e:
            print(f"Error processing {distance} {unit}: {e}")