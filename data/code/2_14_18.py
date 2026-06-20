def convert_to_milliliters(measurements):
    LITERS_TO_ML = 1000.0
    GALLONS_TO_ML = 3785.411784
    CUBIC_INCHES_TO_ML = 16.387064
    
    converted = []
    
    for item in measurements:
        value = item["value"]
        unit = item["unit"]
        
        if value < 0:
            raise ValueError("Volume measurements cannot be negative")
            
        if unit == "liters":
            result = value * LITERS_TO_ML
        elif unit == "gallons":
            result = value * GALLONS_TO_ML
        elif unit == "cubic_inches":
            result = value * CUBIC_INCHES_TO_ML
        else:
            raise ValueError(f"Unknown unit: {unit}")
            
        converted.append({"value": result, "unit": "milliliters"})
        
    return converted

if __name__ == '__main__':
    sample_data = [
        {"value": 1, "unit": "liters"},
        {"value": 2, "unit": "gallons"},
        {"value": 100, "unit": "cubic_inches"},
        {"value": 0, "unit": "liters"}
    ]
    
    results = convert_to_milliliters(sample_data)
    print(results)