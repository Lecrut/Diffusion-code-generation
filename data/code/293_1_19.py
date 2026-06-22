def validate_distance(value, unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    if not isinstance(unit, str) or unit.lower() not in ['km', 'miles']:
        raise ValueError("Unit must be 'km' or 'miles'")

def convert_km_to_miles(kilometers):
    validate_distance(kilometers, 'km')
    return kilometers * 0.621371

def convert_miles_to_km(miles):
    validate_distance(miles, 'miles')
    return miles / 0.621371

if __name__ == '__main__':
    km = 5
    print(f"{km} km is {convert_km_to_miles(km)} miles")
    
    miles = 3
    print(f"{miles} miles is {convert_miles_to_km(miles)} km")