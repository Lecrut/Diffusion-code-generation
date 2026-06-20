import re
from typing import List, Union

def convert_weights_to_kg(weight_list: List[str]) -> List[Union[float, str]]:
    results = []
    
    patterns = [
        (r'^([\d.]+)\s*(g|kg|lb|oz|t|ton)$', lambda m: (float(m.group(1)), m.group(2).lower())),
        (r'^([\d.]+)\s*(grams|kilograms|pounds|ounces|tons|tonnes)$', lambda m: (float(m.group(1)), m.group(2).lower()))
    ]
    
    conversions = {
        'g': 0.001,
        'kg': 1.0,
        'lb': 0.453592,
        'oz': 0.0283495,
        't': 1000.0,
        'ton': 907.185,
        'tonnes': 1000.0,
        'grams': 0.001,
        'kilograms': 1.0,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'tons': 907.185
    }
    
    for item in weight_list:
        if not isinstance(item, str):
            results.append(f"Error: Input '{item}' is not a string.")
            continue
            
        item = item.strip()
        if not item:
            results.append("Error: Empty string provided.")
            continue
            
        converted = False
        for pattern, extractor in patterns:
            match = re.fullmatch(pattern, item)
            if match:
                try:
                    value = extractor(match)
                    val = value[0]
                    unit = value[1]
                    
                    if unit in conversions:
                        kg_value = val * conversions[unit]
                        results.append(kg_value)
                        converted = True
                        break
                    else:
                        results.append(f"Error: Unsupported unit '{unit}'.")
                        converted = True
                        break
                except ValueError:
                    results.append(f"Error: Invalid number format in '{item}'.")
                    converted = True
                    break
        
        if not converted:
            results.append(f"Error: Could not parse '{item}'.")
            
    return results

if __name__ == '__main__':
    weights = [
        "1000 g",
        "5 kg",
        "10 lb",
        "32 oz",
        "2 tons",
        "invalid",
        "",
        "5.5 grams",
        "100 kg"
    ]
    
    result = convert_weights_to_kg(weights)
    print(result)