import sys
def parse_mass(value: str) -> float:
    try:
        return float(value.strip())
    except ValueError:
        raise ValueError(f"Invalid mass value: {value}")
def get_unit(unit_str: str) -> str:
    unit = unit_str.lower().strip()
    if unit in ['kg', 'kilogram', 'kilo']:
        return 'kg'
    elif unit in ['lb', 'pound', 'lbs', 'lbrt']:
        return 'lb'
    else:
        raise ValueError(f"Unsupported unit: {unit_str}")
def convert_to_kg(mass_value: float, mass_unit: str) -> float:
    if mass_unit == 'kg':
        return mass_value
    elif mass_unit == 'lb':
        return mass_value * 0.45359237
    else:
        raise ValueError(f"Unknown unit for conversion: {mass_unit}")
def calculate_weight_difference(masses_data) -> dict:
    kg_values = []
    lb_values = []
    for item in masses_data:
        try:
            mass_value = parse_mass(item['value'])
            if mass_value < 0:
                raise ValueError(f"Negative mass not allowed for {item.get('name', 'unknown')}")
            unit = get_unit(item['unit'])
            converted_kg = convert_to_kg(mass_value, unit)
            kg_values.append(converted_kg)
        except (ValueError, KeyError) as e:
            print(f"Error processing item {item.get('name', 'unknown')}: {e}")
            sys.exit(1)
    if not kg_values:
        return {"error": "No valid items found"}
    total_kg = sum(kg_values)
    differences = []
    for i in range(len(kg_values)):
        diff = abs(total_kg - kg_values[i])
        differences.append({
            'item_index': i,
            'difference_from_total_kg': round(diff, 4),
            'original_unit': item['unit'] if isinstance(item, dict) else 'unknown'
        })
    return {
        "total_mass_kg": round(total_kg, 2),
        "individual_differences": differences
    }
if __name__ == '__main__':
    sample_items = [
        {'value': '10', 'unit': 'kg'},
        {'value': '5.5', 'unit': 'lb'},
        {'value': '20', 'unit': 'kilogram'},
        {'value': '3', 'unit': 'lbs'}
    ]
    result = calculate_weight_difference(sample_items)
    print("Weight Difference Calculation Results")
    print(f"Total Mass: {result['total_mass_kg']} kg")
    if "error" in result:
        print(result["error"])
    else:
        for diff in result.get('individual_differences', []):
            item_name = sample_items[diff['item_index']].get('name', 'Item')
            original_unit = sample_items[diff['item_index']]['unit']
            print(f"Difference from total ({original_unit}): {diff['difference_from_total_kg']} kg")