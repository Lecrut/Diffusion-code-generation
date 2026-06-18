import math

class DistanceNormalizer:
    """Handles conversion of various distance units to meters."""
    
    # Conversion factors from unit to base (meters)
    CONVERSIONS = {
        'meter': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mile': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
    }

    def __init__(self):
        self.conversions = DistanceNormalizer.CONVERSIONS.copy()

    def convert_to_meters(self, value: float | int, unit: str) -> float:
        """Converts a distance in the given unit to meters.
        
        Args:
            value (float|int): The magnitude of the distance.
            unit (str): The string representation of the unit. Supported units are 
                        'meter', 'km', 'cm', 'mm', 'mile', 'yd', 'ft', 'in'.
                        
        Returns:
            float: The distance in meters.
            
        Raises:
            ValueError: If an unsupported or invalid unit is provided.
        """
        if not isinstance(value, (int | float)):
            raise TypeError(f"Value must be a number, got {type(value).__name__}")
        
        normalized_unit = unit.lower().strip()

        if normalized_unit not in self.conversions:
            valid_units = ", ".join(self.CONVERSIONS.keys())
            error_msg = f"Unsupported or invalid unit '{normalized_unit}'. Supported units are:" \
                        f"{valid_units}"
            raise ValueError(error_msg)

        return value * self.conversions[normalized_unit]

def normalize_distance(value: float | int, unit: str) -> tuple[float, dict]:
    """Public function to normalize distance. Returns (meters_in_meters, conversion_info)."""
    
    normalizer = DistanceNormalizer()
    meters = normalizer.convert_to_meters(value, unit)

    return meters, {"original_value": value, "unit": unit}

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (100, 'm'),       # 100 meters -> expected: 100 m
        (5, 'km'),        # 5 km -> expected: 5000 m
        (2000, 'cm'),     # 2000 cm -> expected: 20.0 m
        (1, 'mile'),      # 1 mile -> expected: ~1609.344 m
        (3, 'yd'),        # 3 yards -> expected: ~2.7432 m
    ]

    results = []

    for val_str, unit_str in samples:
        try:
            value = float(val_str) if not isinstance(val_str, int) else int(val_str)
            
            meters, info = normalize_distance(value, unit_str)
            
            # Format output clearly without markdown fences outside code block.
            results.append({
                "input": f"{value} {unit_str}",
                "output_meters": round(meters, 4),
                "info": info
            })

        except Exception as e:
            print(f"Error processing sample '{val_str}' in unit '{unit_str}':", str(e))

    # Print results to stdout for verification.
    for res in results:
        print(f"{res['input']} -> {res['output_meters']:.4f} meters")