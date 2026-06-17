def volume_converter(volume, unit):
    if unit == "L_to_gal":
        if volume["liters"] is not None:
            gallons = volume["liters"] / 3.78541
            return {"result": gallons, "unit": "gallons"}
        else:
            return {"error": "Invalid input for liters"}
    elif unit == "gal_to_L":
        if volume["gallons"] is not None:
            liters = volume["gallons"] * 3.78541
            return {"result": liters, "unit": "liters"}
        else:
            return {"error": "Invalid input for gallons"}
    else:
        return {"error": "Invalid unit specified"}
if __name__ == '__main__':
    sample_data = {
        "L_to_gal": {"liters": 10.0},
        "gal_to_L": {"gallons": 5.0}
    }
    print("--- Testing Liters to Gallons ---")
    conversion1 = volume_converter(sample_data["L_to_gal"], "L_to_gal")
    print(conversion1)
    print("\n--- Testing Gallons to Liters ---")
    conversion2 = volume_converter(sample_data["gal_to_L"], "gal_to_L")
    print(conversion2)