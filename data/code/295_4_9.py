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
    test_liters = 5.0
    test_gallons = volume_converter({"liters": test_liters}, "L_to_gal")
    print(f"\nConverting {test_liters} Liters to Gallons:")
    print(test_gallons)
    test_gallons_only = {"gallons": 10.0}
    test_gallons_to_liters = volume_converter(test_gallons_only, "gal_to_L")
    print(f"\nConverting {test_gallons_only['gallons']} Gallons to Liters:")
    print(test_gallons_to_liters)