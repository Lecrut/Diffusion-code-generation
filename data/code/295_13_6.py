GALLONS_TO_LITERS_FACTOR = 3.78541
LITERS_TO_GALLONS_FACTOR = 1 / GALLONS_TO_LITERS_FACTOR

def gallons_to_liters(gallons):
    return gallons * GALLONS_TO_LITERS_FACTOR

def liters_to_gallons(liters):
    return liters * LITERS_TO_GALLONS_FACTOR

if __name__ == '__main__':
    print(gallons_to_liters(1))
    print(liters_to_gallons(1))