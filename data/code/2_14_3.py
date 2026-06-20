CONVERSION_FACTORS = {
    "liter": 1000.0,
    "gallon": 3785.411784,
    "cubic_inch": 16.387064
}

def convert_volumes_to_ml(volumes):
    results = []
    for item in volumes:
        value = item["value"]
        unit = item["unit"].lower().replace(" ", "_").replace("-", "_")
        
        if unit not in CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {item['unit']}")
        
        if value < 0:
            raise ValueError(f"Negative volume not allowed: {value} {item['unit']}")
        
        if value == 0:
            results.append({"original": item, "ml": 0.0})
        else:
            factor = CONVERSION_FACTORS[unit]
            ml_value = value * factor
            results.append({"original": item, "ml": ml_value})
    
    return results

if __name__ == "__main__":
    sample_data = [
        {"value": 1.0, "unit": "liter"},
        {"value": 0.5, "unit": "gallon"},
        {"value": 100.0, "unit": "cubic inches"},
        {"value": 0, "unit": "liter"},
        {"value": 2.5, "unit": "Liters"}
    ]
    
    output = convert_volumes_to_ml(sample_data)
    for entry in output:
        print(entry)