def liters_to_milliliters(val):
    return val * 1000

def liters_to_cubic_meters(val):
    return val * 0.001

def liters_to_gallons(val):
    return val * 0.264172

def liters_to_cubic_inches(val):
    return val * 61.0237

def milliliters_to_liters(val):
    return val / 1000

def cubic_meters_to_liters(val):
    return val * 1000

def gallons_to_liters(val):
    return val / 0.264172

def cubic_inches_to_liters(val):
    return val / 61.0237

def main():
    liters_input = 5.0
    ml_result = liters_to_milliliters(liters_input)
    print(ml_result)
    m3_result = liters_to_cubic_meters(liters_input)
    print(m3_result)
    gal_result = liters_to_gallons(liters_input)
    print(gal_result)
    ci_result = liters_to_cubic_inches(liters_input)
    print(ci_result)
    gal_input = 10.0
    l_from_gal = gallons_to_liters(gal_input)
    print(l_from_gal)
    ci_input = 300.0
    l_from_ci = cubic_inches_to_liters(ci_input)
    print(l_from_ci)

if __name__ == '__main__':
    main()