import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def metric_to_imperial(measurements):
    results = {}
    for item in measurements:
        if isinstance(item, tuple) and len(item) == 2:
            metric_value, unit = item
            if unit.lower() == 'c':
                fahrenheit = celsius_to_fahrenheit(metric_value)
                results[f"{metric_value}C"] = f"{fahrenheit:.2f}F"
            elif unit.lower() == 'f':
                results[f"{metric_value}C"] = f"{celsius_to_fahrenheit(metric_value):.2f}F"
            else:
                results[f"{metric_value}":] = "Unknown Unit"
        elif isinstance(item, (int, float)):
            fahrenheit = celsius_to_fahrenheit(item)
            results[f"{item}C"] = f"{fahrenheit:.2f}F"
        else:
            results[str(item)] = "Invalid Format"
    return results
if __name__ == '__main__':
    sample_measurements = [
        10,           
        25.5,          
        0,            
        37.0,          
        50,           
        86,                                                                     
        -40
    ]
    converted_data = metric_to_imperial(sample_measurements)
    for metric, imperial in converted_data.items():
        print(f"{metric}: {imperial}")