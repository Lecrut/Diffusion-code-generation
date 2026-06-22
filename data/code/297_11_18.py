GALLONS_TO_LITERS = 3.78541
LITERS_TO_GALLONS = 1 / GALLONS_TO_LITERS

def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == 'gallons' and to_unit == 'liters':
        return round(value * GALLONS_TO_LITERS, 2)
    elif from_unit == 'liters' and to_unit == 'gallons':
        return round(value * LITERS_TO_GALLONS, 2)
    else:
        raise ValueError("Unsupported conversion between units")

if __name__ == '__main__':
    print(f"10 gallons to liters: {convert(10.0, 'gallons', 'liters')}")
    print(f"5 liters to gallons: {convert(5.0, 'liters', 'gallons')}")