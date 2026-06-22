UNIT_CONVERSIONS = {
    "cubic_cm": 1.0,
    "cubic_m": 1000000.0,
    "liters": 1000.0
}

def calculate_prism_volume(base_area, height, unit="cubic_cm"):
    raw_volume = base_area * height
    conversion_factor = UNIT_CONVERSIONS.get(unit, 1.0)
    return raw_volume / conversion_factor

if __name__ == '__main__':
    sample_base = 24.0
    sample_height = 12.5
    computed_volume = calculate_prism_volume(sample_base, sample_height, "cubic_m")
    print(computed_volume)