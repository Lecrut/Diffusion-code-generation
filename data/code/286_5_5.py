def bidirectional_conversion(value, unit):
    if unit == "to_miles":
        return value * 0.000621371
    elif unit == "to_meters":
        return value / 0.000621371
    else:
        raise ValueError("Invalid unit specified. Use 'to_miles' or 'to_meters'.")
if __name__ == '__main__':
    meters = 100
    miles = bidirectional_conversion(meters, "to_miles")
    print(f"{meters} meters is approximately {miles} miles")
    miles_input = 5
    meters_output = bidirectional_conversion(miles_input, "to_meters")
    print(f"{miles_input} miles is approximately {meters_output} meters")