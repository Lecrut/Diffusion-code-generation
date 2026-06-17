import json
import sys
def parse_input():
    if len(sys.argv) > 1:
        try:
            data = json.loads(sys.argv[1])
            return {
                'volume': float(data.get('value', 0)),
                'unit': str(data.get('from_unit', 'liters')).lower(),
                'to_units': [str(u).lower() for u in data.get('target_units', ['ml', 'gallons'])]
            }
        except json.JSONDecodeError:
            return {
                'volume': float(sys.argv[1]),
                'unit': str(sys.argv[2]).lower(),
                'to_units': [str(u).lower() for u in sys.argv[3].split(',') if len(sys.argv) > 4 and i < len(sys.argv)] if len(sys.argv) == 5 else ['ml', 'gallons']
            }
    return {
        'volume': float('0'),
        'unit': str('liters').lower(),
        'to_units': [str(u).lower() for u in ['milliliters', 'fluid_ounces', 'gallons']]
    }
def convert_volume(value, from_unit):
    liters = 1.0 if from_unit == 'liters' else (value / 1000) if from_unit == 'kiloliters' else value * 1000
    return {
        'milliliters': round(liters * 1000, 2),
        'fluid_ounces': round(liters * 33.814, 2),
        'gallons': round(liters / 264.172, 2)
    }
def format_output(data):
    conversions = convert_volume(data['volume'], data['unit'])
    output_lines = [f"Input: {data['value']} {data['unit'].upper()}"]
    for unit in data['to_units']:
        if 'milliliters' in unit or 'ml' == unit:
            key = 'milliliters'
        elif 'ounces' in unit or 'fl_oz' == unit:
            key = 'fluid_ounces'
        else:
            key = 'gallons'
        output_lines.append(f"{unit.capitalize()}: {conversions[key]:.2f}")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    try:
        input_data = parse_input()
        result_str = format_output(input_data)
        print(result_str)
    except Exception as e:
        pass