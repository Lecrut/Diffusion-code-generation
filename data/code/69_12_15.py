def _validate_non_negative(value: float) -> None:
    if value < 0:
        raise ValueError("Miles cannot be negative")

def miles_to_feet_calc(miles: float) -> float:
    _validate_non_negative(miles)
    conversion_factor: int = 5280
    return miles * conversion_factor

if __name__ == '__main__':
    input_distance: float = 12.5
    output_feet: float = miles_to_feet_calc(input_distance)
    print(output_feet)