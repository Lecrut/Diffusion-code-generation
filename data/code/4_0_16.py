def convert_distance(value, from_unit, to_unit):
    if value < 0:
        raise ValueError("Distance cannot be negative.")
    
    factors = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.344,
    }
    
    units = set(factors.keys())
    
    if from_unit not in units:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Unknown target unit: {to_unit}")
    
    meters = value * factors[from_unit]
    result = meters / factors[to_unit]
    
    return result

if __name__ == '__main__':
    meters = 1000.0
    kilometers = convert_distance(meters, "meters", "kilometers")
    print(kilometers)
    
    miles = convert_distance(kilometers, "kilometers", "miles")
    print(miles)
    
    back_to_meters = convert_distance(miles, "miles", "meters")
    print(back_to_meters)