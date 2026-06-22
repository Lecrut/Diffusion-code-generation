from decimal import Decimal, ROUND_HALF_UP

def feet_to_inches(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a float")
    feet_decimal = Decimal(str(feet))
    conversion_factor = Decimal("12")
    inches_decimal = feet_decimal * conversion_factor
    return float(inches_decimal)

if __name__ == "__main__":
    sample_value = 5.5
    result = feet_to_inches(sample_value)
    print(result)