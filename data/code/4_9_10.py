def convert_distance(value: float, unit: str) -> float:
    miles_to_kilometers = 1.60934
    if unit == "miles":
        return value * miles_to_kilometers
    if unit == "kilometers":
        return value / miles_to_kilometers
    raise ValueError("Unit must be 'miles' or 'kilometers'")

if __name__ == '__main__':
    distance_miles = 10.0
    result_km = convert_distance(distance_miles, "miles")
    print(result_km)
    
    distance_km = 16.0934
    result_miles = convert_distance(distance_km, "kilometers")
    print(result_miles)