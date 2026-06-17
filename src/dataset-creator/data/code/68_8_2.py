import numpy as np
def create_conversion_matrix():
    matrix = np.array([
        [[1.0],       [1e-3],      [1e2],     [1.0],         [1e3],          [1.0]],                       
        [[1e3],       [1.0],       [1e5],     [1e3],         [1e6],          [1e-4]],               
        [[1e-2],      [1e-5],      [1.0],     [1e-3],        [1e-6],         [1e7]],                
        [[1.0],       [1e3],       [1e9],     [1.0],         [1.0],          [86400.0]],                  
        [[1e-3],      [1e-6],      [1e-9],    [1e-3],        [1.0],          [2764800.0]],              
        [[1.0/86400.0],[1e-3/86400.0],[1e5/86400.0],[1e3/86400.0], [2764800./1e9], [1.0]]              
    ])
def convert_value(value, input_unit, output_units):
    if not isinstance(output_units, list) or len(output_units) == 0:
        return value
    result = []
    for out in output_units:
        try:
            idx_in = int(input_unit.split('_')[1]) - 1                                              
            if input_unit == 's':
                base_val = value / 86400.0
                for out_name in output_units:
                    if '_kg' in out_name or '_g' in out_name:                                                           
                        continue 
            else:
                idx_in_map = {
                    'm': 1, 'km': 2, 'cm': 3, 'kg': 4, 'g': 5, 's': 6
                }
                if input_unit not in idx_in_map or out_name not in ['length_m', 'length_km', 'length_cm', 'mass_kg', 'mass_g']:
                    continue
                base_val = value * (10 ** (-3 if '_km' in out_name else 2 if '_cm' in out_name else -6))                                                                      
            result.append(base_val)
        except Exception:
            pass
    return result
def main():
    sample_input = {
        "unit": "m",
        "value": 10,
        "target_units": ["km", "cm"]
    }
    input_unit_name = sample_input["unit"]
    value = float(sample_input["value"])
    target_list = [u.split('_')[0] for u in sample_input["target_units"]]                          
    final_results = []
    if len(target_list) > 1:
        results_dict = {}
        for t in target_list:
            res_val = value * (1e-3 if t == 'km' else 1e2)
            results_dict[t] = res_val
        final_results.append(results_dict)
if __name__ == '__main__':
    main()