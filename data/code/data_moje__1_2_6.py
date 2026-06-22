import re

def convert_to_kilograms(measurements):
    conversion_factors = {
        'kg': 1,
        'kilogram': 1,
        'kilograms': 1,
        'g': 0.001,
        'gram': 0.001,
        'grams': 0.001,
        'lb': 0.45359237,
        'lbs': 0.45359237,
        'pound': 0.45359237,
        'pounds': 0.45359237,
        'oz': 0.028349523125,
        'ounce': 0.028349523125,
        'ounces': 0.028349523125,
        'st': 6.35029318,
        'stone': 6.35029318,
        'stones': 6.35029318
    }
    
    results = []
    
    for item in measurements:
        if not isinstance(item, str):
            results.append(None)
            continue
            
        item = item.strip()
        if not item:
            results.append(None)
            continue
            
        match = re.match(r'^(\d+(?:\.\d+)?)\s*(kg|kilograms?|g|grams?|lb|lbs|pounds?|oz|ounces?|st|stones?)$', item, re.IGNORECASE)
        
        if match:
            try:
                value = float(match.group(1))
                unit = match.group(2).lower()
                if unit in conversion_factors:
                    converted_value = value * conversion_factors[unit]
                    results.append(round(converted_value, 6))
                else:
                    results.append(None)
            except ValueError:
                results.append(None)
        else:
            results.append(None)
            
    return results

if __name__ == '__main__':
    sample_data = [
        "5 kg",
        "1000 g",
        "2.5 lbs",
        "16 oz",
        "1 stone",
        "invalid",
        "100",
        "",
        "abc"
    ]
    
    output = convert_to_kilograms(sample_data)
    print(output)