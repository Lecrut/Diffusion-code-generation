GALLON_TO_LITER = 3.78541
LITER_TO_GALLON = 1 / GALLON_TO_LITER

def gallons_to_liters(gallons: float) -> float:
    return round(gallons * GALLON_TO_LITER, 2)

def liters_to_gallons(liters: float) -> float:
    return round(liters * LITER_TO_GALLON, 2)

if __name__ == '__main__':
    print(f"10 gallons to liters: {gallons_to_liters(10.0)}")
    print(f"5 liters to gallons: {liters_to_gallons(5.0)}")