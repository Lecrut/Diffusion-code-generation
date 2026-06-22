conversion_factors = {
    "gallon": 3.78541,
    "liter": 1.0
}

def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit provided")
    base_value = value * conversion_factors[from_unit]
    result = round(base_value / conversion_factors[to_unit], 2)
    return result

if __name__ == '__main__':
    print(f"10 gallons to liters: {convert(10.0, 'gallon', 'liter')}")
    print(f"5 liters to gallons: {convert(5.0, 'liter', 'gallon')}")
    print(f"2 gallons to gallons: {convert(2.0, 'gallon', 'gallon')}")