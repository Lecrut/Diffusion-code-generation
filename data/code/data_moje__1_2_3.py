import re

def convert_to_kilograms(measurements):
    kg_list = []
    for item in measurements:
        if not isinstance(item, str):
            try:
                val = float(item)
                kg_list.append(val)
                continue
            except (ValueError, TypeError):
                raise ValueError(f"Invalid measurement format: {item}")
        
        match = re.match(r'^\s*(\d+(?:\.\d+)?)\s*(lbs|lb|pounds?|kg|kilograms?|g|grams?)\s*$', item, re.IGNORECASE)
        if not match:
            raise ValueError(f"Could not parse measurement: {item}")
        
        value_str, unit = match.groups()
        value = float(value_str)
        unit_lower = unit.lower()
        
        if unit_lower.startswith('kg') or unit_lower == 'kilogram' or unit_lower.startswith('kilograms'):
            kg_list.append(value)
        elif unit_lower.startswith('g') or unit_lower == 'gram' or unit_lower.startswith('grams'):
            kg_list.append(value / 1000.0)
        elif unit_lower.startswith('l') or unit_lower.startswith('pounds') or unit_lower == 'lb' or unit_lower.startswith('lb'):
            kg_list.append(value * 0.45359237)
        else:
            raise ValueError(f"Unsupported unit: {unit}")
            
    return kg_list

if __name__ == '__main__':
    sample_data = ["70 kg", "150 lbs", "500g", "2.5 pounds", "1000"]
    result = convert_to_kilograms(sample_data)
    print(result)