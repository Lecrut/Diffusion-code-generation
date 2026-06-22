def _get_feet_per_mile() -> float:
    return 5280.0

def miles_to_feet_calc(miles: float) -> float:
    conversion_factor: float = _get_feet_per_mile()
    input_value: float = float(miles)
    calculated_feet: float = input_value * conversion_factor
    return calculated_feet

if __name__ == '__main__':
    test_distance: float = 12.75
    final_result: float = miles_to_feet_calc(test_distance)
    print(final_result)