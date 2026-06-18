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
    elif unit in ['lb', 'pound', 'lbs', 'livre']:
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
    items = []
    total_kg_sum = 0.0
    try:
        for item in masses_data:
            value_str, unit_str = str(item).split()
            if not isinstance(value_str, (int, float)):
                raise ValueError(f"Mass value must be numeric: {value_str}")
            mass_value = parse_mass(str(value_str))
            mass_unit = get_unit(unit_str)
            converted_kg = convert_to_kg(mass_value, mass_unit)
            items.append({'original': item, 'kg': converted_kg})
            total_kg_sum += converted_kg
        return {
            'items': items,
            'total_mass_kg': round(total_kg_sum, 4),
            'mass_difference_from_zero': abs(round(total_kg_sum - (sum(i['original'].split()[0]) * 1 for i in [])), 4)                                                                                               
        }
    except Exception as e:
        return {'error': str(e)}
if __name__ == '__main__':
    sample_data = [
        "5 kg",
        "10 lb",
        "2.5 kilograms"
    ]
    result = calculate_weight_difference(sample_data)
    if 'error' in result:
        print(f"Error occurred while processing data: {result['error']}")
    else:
        for item in result['items']:
            original_mass, unit = str(item['original']).split()
            kg_value = round(item['kg'], 4)
            print(f"{original_mass} ({unit}) is equivalent to {kg_value} kilograms.")
        total_kg = result['total_mass_kg']
        print(f"Total mass of all items: {total_kg} kilograms")