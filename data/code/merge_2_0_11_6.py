import timeit
def compare_types():
    int_var = 100
    float_var = 100.0
    result_int_float = (int_var == float_var)
    return {
        'int_value': int_var,
        'float_value': float_var,
        'comparison_result': result_int_float,
        'types_matched': isinstance(int_var, int) and isinstance(float_var, float),
    }
if __name__ == '__main__':
    data = compare_types()
    print(f"Integer: {data['int_value']} (type: int)")
    print(f"Float:   {data['float_value']} (type: float)")
    print(f"Are they equal? {'Yes' if data['comparison_result'] else 'No'}")