import numpy as np
def create_conversion_matrix():
    matrix = np.array([
        [[1.0],               
         [0.001],                              
         [100.0]],                          
        [[1.0],                 
         [1000.0]],                          
        [[1.0],               
         [0.001]]                             
    ])
def convert_value(input_unit, input_val, output_units):
    if len(output_units) != 2:
        raise ValueError("Output units must be a list of two values")
    try:
        idx = np.where(np.array([input_unit]) == matrix[0])[0][0]
        row_idx = int(input_val) - 1
        result = []
        for out in output_units:
            if len(out) != 2:
                raise ValueError(f"Output unit {out} must be a list of two values")
            try:
                col_idx = np.where(np.array([out]) == matrix[0])[0][0]
                if input_unit == 'm' or output_units[1] == 'km':
                    result.append(input_val * 0.001)
                elif input_unit == 'cm' and output_units[1] == 'm':
                    result.append(input_val / 100)
                else:
                    result.append(input_val)
            except IndexError:
                raise ValueError(f"Unsupported unit conversion from {input_unit} to {out}")
        return result
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None
if __name__ == '__main__':
    test_cases = [
        {'input_unit': 'm', 'input_val': 10, 'output_units': ['km', 'cm']},
        {'input_unit': 'kg', 'input_val': 500, 'output_units': ['g', 'mg']},                                                             
    ]
    for case in test_cases:
        result = convert_value(case['input_unit'], case['input_val'], case['output_units'])
        print(f"Input {case['input_unit']} ({case['input_val']}): Output -> {result}")