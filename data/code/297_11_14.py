def gallons_to_liters(gallons):
    return round(gallons * 3.78541, 2)

def liters_to_gallons(liters):
    return round(liters / 3.78541, 2)
if __name__ == '__main__':
    print(gallons_to_liters(5))
    print(liters_to_gallons(10))