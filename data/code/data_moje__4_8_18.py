def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

if __name__ == '__main__':
    km_value = 10.0
    miles_value = 10.0
    
    miles_from_km = km_to_miles(km_value)
    km_from_miles = miles_to_km(miles_value)
    
    print(f"{km_value} kilometers is {miles_from_km} miles.")
    print(f"{miles_value} miles is {km_from_miles} kilometers.")