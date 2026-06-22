def gallons_to_liters(gallons: float) -> float:
    return round(gallons * 3.78541, 2)

def liters_to_gallons(liters: float) -> float:
    return round(liters / 3.78541, 2)

if __name__ == '__main__':
    gallons_value = 5.0
    liters_value = 20.0
    
    print(f"{gallons_value} gallons to liters: {gallons_to_liters(gallons_value)}")
    print(f"{liters_value} liters to gallons: {liters_to_gallons(liters_value)}")