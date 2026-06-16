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
        "liters": 10.0,
        "gallons": 2.64172
    }
    print("--- Converting Liters to Gallons ---")
    result1 = volume_converter(sample_data, "L_to_gal")
    print(result1)
    print("\n--- Converting Gallons to Liters ---")
    result2 = volume_converter(sample_data, "gal_to_L")
    print(result2)
    sample_data_2 = {
        "liters": 3.78541,
        "gallons": 1.0
    }
    print("\n--- Converting Sample Data (L to Gal) ---")
    result3 = volume_converter(sample_data_2, "L_to_gal")
    print(result3)
    print("\n--- Converting Sample Data (Gal to L) ---")
    result4 = volume_converter(sample_data_2, "gal_to_L")
    print(result4)