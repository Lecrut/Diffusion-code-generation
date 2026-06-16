def volume_converter(volume, unit):
    if unit == "L_to_gal":
        if volume["liters"] is not None:
            gallons = volume["liters"] / 3.78541
            return {"result": gallons, "unit": "gallons"}
    elif unit == "gal_to_L":
        if volume["gallons"] is not None:
            liters = volume["gallons"] * 3.78541
            return {"result": liters, "unit": "liters"}
    return {"error": "Invalid conversion type or missing data"}
if __name__ == '__main__':
    sample_data = {
        "liters": 10,
        "gallons": 20
    }
    print("--- Liters to Gallons ---")
    conversion_result_1 = volume_converter(sample_data, "L_to_gal")
    print(f"10 Liters is {conversion_result_1.get('result', 'Error')} {conversion_result_1.get('unit', '')}")
    print("\n--- Gallons to Liters ---")
    conversion_result_2 = volume_converter(sample_data, "gal_to_L")
    print(f"20 Gallons is {conversion_result_2.get('result', 'Error')} {conversion_result_2.get('unit', '')}")
    sample_data_2 = {"liters": 37.8541, "gallons": 10}
    print("\n--- Specific Conversion Test (10 Gallons) ---")
    conversion_result_3 = volume_converter(sample_data_2, "gal_to_L")
    print(f"10 Gallons is {conversion_result_3.get('result', 'Error')} {conversion_result_3.get('unit', '')}")