import sys

def convert_measurements(lengths, source_unit):
    if source_unit not in ["km", "m", "ft"]:
        return {"error": "Unsupported unit. Use 'km', 'm', or 'ft'."}
    
    conversion_to_meters = {
        "km": 1000.0,
        "m": 1.0,
        "ft": 0.3048
    }
    
    meters_per_foot = 0.3048
    
    results = []
    for length in lengths:
        try:
            value = float(length)
            if value < 0:
                results.append({"input": str(length), "error": "Negative values not allowed"})
                continue
            
            meters = value * conversion_to_meters[source_unit]
            feet = meters / meters_per_foot
            
            results.append({
                "input": str(length),
                "input_unit": source_unit,
                "meters": round(meters, 4),
                "feet": round(feet, 4)
            })
        except ValueError:
            results.append({"input": str(length), "error": "Invalid number format"})
    
    return results

if __name__ == "__main__":
    sample_data = ["5", "1.5", "100", "0.01"]
    target_unit = "km"
    output = convert_measurements(sample_data, target_unit)
    
    print(f"Converting {sample_data} from {target_unit}:")
    for item in output:
        if "error" in item and item["error"]:
            print(f"Input: {item['input']} -> Error: {item['error']}")
        else:
            print(f"Input: {item['input']} {item['input_unit']} -> {item['meters']} meters, {item['feet']} feet")