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
    print(f"{meters} meters is equal to {miles} miles")
    miles_to_convert = 5
    meters_from_miles = bidirectional_conversion(miles_to_convert, "to_meters")
    print(f"{miles_to_convert} miles is equal to {meters_from_miles} meters")
    meters_large = 1000
    miles_from_large = bidirectional_conversion(meters_large, "to_miles")
    print(f"{meters_large} meters is equal to {miles_from_large} miles")