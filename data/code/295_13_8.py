GALLONS_TO_LITERS = 3.78541

def gallons_to_liters(gallons):
    return gallons * GALLONS_TO_LITERS

def liters_to_gallons(liters):
    return liters / GALLONS_TO_LITERS

if __name__ == '__main__':
    print(gallons_to_liters(1))
    print(liters_to_gallons(3.78541))