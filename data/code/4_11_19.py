def adjust_distance(distance, unit_type):
    if unit_type == "miles":
        adjusted = distance * 1.60934
        return adjusted, "km"
    elif unit_type == "km":
        adjusted = distance * 0.621371
        return adjusted, "miles"
    else:
        raise ValueError(f"Unsupported unit: {unit_type}")

if __name__ == "__main__":
    distance_value = 10
    unit = "miles"
    result, new_unit = adjust_distance(distance_value, unit)
    print(f"{distance_value} {unit} = {result} {new_unit}")

    distance_value = 10
    unit = "km"
    result, new_unit = adjust_distance(distance_value, unit)
    print(f"{distance_value} {unit} = {result} {new_unit}")