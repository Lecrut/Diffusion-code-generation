def convert_length(length, unit):
    conversions = {
        "meters": length,
        "feet": length * 3.28084,
        "kilometers": length * 1000
    }
    supported_units = {"meters", "feet", "kilometers"}
    if unit in supported_units:
        return conversions[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    try:
        result1 = convert_length(10, "meters")
        print(f"10 meters is {result1} meters")
        result2 = convert_length(10, "feet")
        print(f"10 meters is {result2} feet")
        result3 = convert_length(1, "kilometers")
        print(f"1 kilometer is {result3} kilometers")
        result4 = convert_length(5, "miles")
    except ValueError as e:
        print(f"Error caught: {e}")