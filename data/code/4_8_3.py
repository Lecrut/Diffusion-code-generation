def convert_kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

def convert_miles_to_kilometers(miles):
    kilometers = miles / 0.621371
    return kilometers

def run_conversion_tool(distance, source_unit, target_unit):
    if source_unit == "km" and target_unit == "mi":
        result = convert_kilometers_to_miles(distance)
        return f"{distance} kilometers is {result:.2f} miles"
    elif source_unit == "mi" and target_unit == "km":
        result = convert_miles_to_kilometers(distance)
        return f"{distance} miles is {result:.2f} kilometers"
    else:
        raise ValueError("Invalid unit conversion requested. Use km to mi or mi to km.")

if __name__ == "__main__":
    sample_distance_km = 100
    sample_distance_mi = 50
    print(run_conversion_tool(sample_distance_km, "km", "mi"))
    print(run_conversion_tool(sample_distance_mi, "mi", "km"))