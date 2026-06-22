def validate_measurements(nanometers, micrometers):
    if not isinstance(nanometers, (int, float)) or not isinstance(micrometers, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if nanometers < 0 or micrometers < 0:
        raise ValueError("Measurements cannot be negative")

def compare_measures(nanometers, micrometers):
    validate_measurements(nanometers, micrometers)
    conversion_factor = 1000
    if nanometers < micrometers * conversion_factor:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_measures(500, 2))