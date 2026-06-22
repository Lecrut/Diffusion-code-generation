def gallons_to_liters(gallons):
    return round(gallons * 3.78541, 2)

def liters_to_gallons(liters):
    return round(liters / 3.78541, 2)

if __name__ == '__main__':
    print(f"10 gallons to liters: {gallons_to_liters(10)}")
    print(f"20 liters to gallons: {liters_to_gallons(20)}")