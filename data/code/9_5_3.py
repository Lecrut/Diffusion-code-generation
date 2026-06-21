from decimal import Decimal, getcontext

getcontext().prec = 50

CONVERSION_FACTORS = {
    "liter": Decimal("1"),
    "liters": Decimal("1"),
    "l": Decimal("1"),
    "ml": Decimal("0.001"),
    "milliliter": Decimal("0.001"),
    "milliliters": Decimal("0.001"),
    "us_gallon": Decimal("3.785411784"),
    "us_gal": Decimal("3.785411784"),
    "gallon_us": Decimal("3.785411784"),
    "us_quart": Decimal("0.946352946"),
    "quart_us": Decimal("0.946352946"),
    "us_pint": Decimal("0.473176473"),
    "pint_us": Decimal("0.473176473"),
    "us_cup": Decimal("0.24"),
    "cup_us": Decimal("0.24"),
    "us_fl_oz": Decimal("0.0295735295625"),
    "fl_oz_us": Decimal("0.0295735295625"),
    "imperial_gallon": Decimal("4.54609"),
    "imp_gallon": Decimal("4.54609"),
    "gallon_uk": Decimal("4.54609"),
    "imperial_quart": Decimal("1.1365225"),
    "quart_uk": Decimal("1.1365225"),
    "imperial_pint": Decimal("0.56826125"),
    "pint_uk": Decimal("0.56826125"),
    "imperial_fl_oz": Decimal("0.0284130625"),
    "fl_oz_uk": Decimal("0.0284130625"),
    "cubic_meter": Decimal("1000"),
    "cubic_centimeter": Decimal("0.001"),
    "cc": Decimal("0.001"),
    "cubic_inch": Decimal("0.016387064"),
    "cubic_foot": Decimal("28.316846592"),
    "barrel_oil": Decimal("158.987294928"),
    "barrel": Decimal("158.987294928"),
}

def convert_volume_to_liters(value: float, unit: str) -> Decimal:
    unit_lower = unit.lower().replace("_", "").replace("-", "").replace(" ", "")
    
    normalized_unit = None
    for key in CONVERSION_FACTORS:
        k_clean = key.replace("_", "").replace("-", "").replace(" ", "").lower()
        if k_clean == unit_lower:
            normalized_unit = key
            break
    
    if normalized_unit is None:
        raise ValueError(f"Unsupported unit: {unit}")
    
    factor = CONVERSION_FACTORS[normalized_unit]
    return Decimal(str(value)) * factor

if __name__ == "__main__":
    sample_values = [
        (1, "us_gallon"),
        (1, "imperial_gallon"),
        (250, "ml"),
        (1.5, "cubic_meter"),
        (100, "barrel_oil"),
    ]
    
    for val, unit in sample_values:
        result = convert_volume_to_liters(val, unit)
        print(f"{val} {unit} = {result} liters")