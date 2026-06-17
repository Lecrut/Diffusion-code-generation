import numpy as np
def create_conversion_matrix():
    matrix = np.array([
        [[1.0],       [1e-3],      [1e2],     [1.0/9.80665*1000],                                                                                                                                                 
         ], 
        [[1e3],       [1.0],      [1e-2],     [],          []]
    ])
def convert_units(input_value, input_unit, output_unit):
    unit_map = {
        'm': 0, 'km': 1, 'cm': 2, 
        'kg': 3, 'g': 4, 
        's': 5
    }
    if input_unit not in unit_map or output_unit not in unit_map:
        raise ValueError("Invalid units")
    if input_unit == output_unit:
        return input_value
    conversions = {
        ('m', 'km'): lambda x, y: x * 1000 / (y or 1),
        ('m', 'cm'): lambda x, y: x * 100 / (y or 1),
        ('kg', 'g'): lambda x, y: x * 1000 / (y or 1),
    }
    factor = {
        ('m', 'km'): 1e-3,
        ('m', 'cm'): 1e2,
        ('kg', 'g'): 1e-3,
        ('g', 'kg'): 1e3,
    }
    return input_value * factor.get((input_unit, output_unit), None) or (lambda x: x if input_unit == output_unit else float('nan'))(input_value)
if __name__ == '__main__':
    samples = [
        {'value': 100.5, 'from': 'm', 'to': 'km'},
        {'value': 2500.0, 'from': 'kg', 'to': 'g'},
        {'value': 3.7, 'from': 'cm', 'to': 'mm'}                                            
    ]
    results = []
    for s in samples:
        try:
            result_value = convert_units(s['value'], s['from'], s['to'])
            if isinstance(result_value, float) and np.isnan(result_value):
                print(f"Error converting {s['value']} {s['from']} to {s['to']}: Invalid factor")
            else:
                results.append({'input': f"{s['value']} {s['from']}", 'output': f"{result_value} {s['to']}"})
        except Exception as e:
            print(f"Error processing sample {s}: {e}")
    for r in results:
        print(r)