from typing import List, Dict, Union
def convert_to_base(value: float, unit: str) -> float:
    base_kg = 0.0
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string.")
    valid_units = ['kg', 'g', 'lbs']
    if unit.lower() not in valid_units:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are {valid_units}.")
    if unit == 'kg':
        base_kg = value * 1.0
    elif unit == 'g':
        base_kg = value / 1000.0
    elif unit == 'lbs':
        base_kg = value * 0.45359237
    return base_kg
def calculate_difference(data: Union[List[Dict], Dict]) -> List[Dict]:
    if isinstance(data, dict):
        items = [data]
    elif isinstance(data, (list, tuple)):
        items = []
        for item in data:
            if not isinstance(item, (dict, float)) and len(str(item).split(':')) != 2:
                raise ValueError("Invalid mass entry format. Expecting 'value:unit' or dict.")
            try:
                value_str, unit_str = str(item).split(':')
                val_float = float(value_str.strip())
                unit_lower = unit_str.lower().strip() if isinstance(unit_str, str) else "kg"
                converted_kg = convert_to_base(val_float, unit_lower)
                items.append({
                    'original_value': val_float,
                    'original_unit': unit_lower,
                    'converted_base_kg': converted_kg
                })
            except (ValueError, AttributeError):
                raise ValueError(f"Invalid mass entry: {item}")
    else:
        raise TypeError("Input must be a list or dictionary.")
    if len(items) < 2:
        return []
    base_value = items[0]['converted_base_kg']
    differences = []
    for i in range(len(items)):
        item_diffs = []
        diff_items = [j for j in range(1, len(items)) if j != i]
        for idx_j in diff_items:
            val_i_kg = items[i]['converted_base_kg']
            val_j_kg = items[idx_j]['converted_base_kg']
            item_diffs.append({
                'index': f"{i}-{idx_j}",
                'value_a': {
                    'amount': abs(val_i_kg - base_value),
                    'unit': items[i]['original_unit'],
                    'direction': "difference from baseline" if val_i_kg != base_value else 0.0,
                    'converted_base_kg': items[i]['converted_base_kg']
                },
                'value_b': {
                    'amount': abs(val_j_kg - base_value),
                    'unit': items[idx_j]['original_unit'],
                    'direction': "difference from baseline" if val_j_kg != base_value else 0.0,
                    'converted_base_kg': items[idx_j]['converted_base_kg']
                }
            })
        differences.append({
            'index': i,
            'differences': item_diffs
        })
    return differences
if __name__ == '__main__':
    sample_data = [
        "50:kg",
        "1234:g",
        "68.7:lbs"
    ]
    result = calculate_difference(sample_data)
    print("Difference Results:")
    for item in result:
        print(f"\nIndex {item['index']}:")
        for diff in item['differences']:
            a = diff['value_a']['amount']
            b = diff['value_b']['amount']
            u1 = diff['value_a']['unit']
            u2 = diff['value_b']['unit']
            print(f"  Entry A ({u1}): {a:.4f} kg")
            print(f"  Entry B ({u2}): {b:.4f} kg")