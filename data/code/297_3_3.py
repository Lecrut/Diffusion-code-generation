import math
def convert_dimensions(measurements, target_unit):
    conversions = {}
    for value, unit in measurements:
        if unit == "meter" and target_unit == "kilogram":
            if "pound" in unit:
                conversion_factor = 0.453592
                converted_value = value * conversion_factor
                conversions[f"{value} {unit}"] = converted_value
            elif "meter" in unit:
                if target_unit == "meter":
                    conversions[f"{value} {unit}"] = value
                elif target_unit == "kilogram":
                    conversions[f"{value} {unit}"] = value                                                        
                else:
                    conversions[f"{value} {unit}"] = value
            else:
                conversions[f"{value} {unit}"] = value
        elif target_unit == "meter" and unit == "meter":
             conversions[f"{value} {unit}"] = value
        elif target_unit == "pound" and unit == "pound":
             conversions[f"{value} {unit}"] = value
        else:
            conversions[f"{value} {unit}"] = value
    return conversions
if __name__ == '__main__':
    sample_measurements = [
        (10.0, "meter"),
        (200.0, "pound"),
        (5.0, "meter")
    ]
    target = "kilogram"
    results = convert_dimensions(sample_measurements, target)
    print(results)