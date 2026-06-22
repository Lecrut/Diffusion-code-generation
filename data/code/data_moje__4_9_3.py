def convert_distance(value, unit):
    if unit == "miles":
        return value * 1.60934
    if unit == "kilometers":
        return value / 1.60934
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    miles_to_km = convert_distance(10, "miles")
    km_to_miles = convert_distance(16.0934, "kilometers")
    print(miles_to_km)
    print(km_to_miles)